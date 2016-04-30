from __future__ import print_function

from quest_core import parse
from quest_core import Requirement
from quest_core import Task
from quest_core import GameState

from settings import Devices
from settings import Global

from deviceMaster.devicemaster import DeviceMaster

import time
import threading
import tornado
import subprocess
import pygame
import platform
if platform.system() == 'Windows':
    from KeyboardListener import KeyboardListener

from full_quest import *



clients = None
master = None
class QuestRoom(threading.Thread):

    def __init__(self, cli):
        global clients
        clients = cli
        self.game_state = None

        # sound_manager = None
        # pygame.mixer.init()
        # self.ambient_music = pygame.mixer.Sound("game_ambient.wav")
        # self.final_game_music = pygame.mixer.Sound("final_game.wav")
        # self.win_music = pygame.mixer.Sound("you_win.wav")
        # self.current_music = self.ambient_music

        self.last_sended_messages = {}

        super(QuestRoom, self).__init__()

    def run(self):
        print("quest room thread start")
        global master
        master = DeviceMaster()

        if platform.system() == 'Windows':
            lovecraft_comport = Devices.LOVECRAFT_DEVICE_COM_PORT_WIN
        else:
            if master.debugMode():
                lovecraft_comport = Devices.LOVECRAFT_DEVICE_COM_PORT_WIN
            else:
                lovecraft_comport = "/dev/ttyUSB2"
                bashCommand = Global.GET_TTY_USB_SCRIPT + Devices.LOVECRAFT_USB_SERIAL_NUMBER
                process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

                lovecraft_comport = process.communicate()[0]
            print("Use COM-port: {}".format(lovecraft_comport))

        self.lovecraft_device = master.addSlave(Devices.LOVECRAFT_DEVICE_NAME, lovecraft_comport, 1, boudrate=0)

        master.start()

        self.game_state = parse(Global.SCENARY_FILE)

        self.game_state.device_master = master
        self.game_state.slave = self.lovecraft_device
        self.game_state.quest_room = self
        self.game_state.start_game_loop(self.send_state)


    def set_door_state(self, door_id, door_state):
        relays = master.getRelays(self.captainsBridge_2).get()
        relays[door_id] = door_state
        master.setRelays(self.captainsBridge_2, relays)

    def set_box_state(self, box_id, box_state):
        smartLeds = master.getSmartLeds(self.hallwayPuzzles)
        if(box_state == 0):
            smartLeds.setOneLed(box_id + 8, Colors.BLUE)
        else:
            smartLeds.setOneLed(box_id + 8, Colors.RED)
        relays = master.getRelays(self.hallwayPuzzles).get()
        relays[box_id] = box_state
        master.setRelays(self.hallwayPuzzles, relays)

    def send_ws_message(self, client_id, message):
        # print("send_ws_message: to client {}".format(client_id))
        str_id = str(client_id)
        if str_id not in clients: return
        if 'progress_visible' not in message: message['progress_visible'] = True
        if 'countdown_active' not in message: message['countdown_active'] = True

        clients[str_id]['object'].write_message(message)

        # save last sended message
        self.last_sended_messages[str_id] = message

    def send_state(self, message):
        if self.game_state is None:
            return

        message = {'message': [u" ({}).{}".format(x.id, x.title).encode('utf-8') for x in self.game_state.active_tasks]}
        message = tornado.escape.json_encode(message)
        try:
            if '42' in clients:
                clients['42']['object'].write_message(message)
        except:
            pass

    def toggle_skiped_task(self, task_id):
        """ Skip or unskip task from questlogic"""
        for task in self.game_state.tasks:
            if task_id == task.id:
                if task in self.game_state.skipped_tasks:
                    self.game_state.skipped_tasks.remove(task)
                else:
                    self.game_state.skipped_tasks.append(task)

    def turn_light(self, light_id):
        global master
        if light_id == "onAll":
            # print("Command to light all")
            AC_ENABLE_ALL_LIGHT(master, None, None)
        elif light_id == "offAll":
            # print("Command to light off")
            AC_DISABLE_ALL_LIGHT(master, None, None)
        elif light_id == "startOn":
            # print("Command light to start ")
            AC_ENABLE_INIT_LIGHTS(master, None, None)
        elif light_id == "wireOn":
            # print("Command light to wireConnected ")
            AC_ENABLE_WIRE_ROOMS_LIGHT(master, None, None)
        elif light_id == "fuseOn":
            # print("Command light to fuse insert ")
            AC_ENABLE_FUSE_ROOMS_LIGHT(master, None, None)

    def set_room_light(self, room_led_id, in_color):
        # convert color range from 255 to 4096
        color = [value * 16 for value in in_color]
        # print("Color {} in new range {}".format(in_color, color))

        if room_led_id == "entrance_top":
            setRoomLight(master, ROOM_LEDS.ENTRANCE_TOP, color)

        elif room_led_id == "entrance_bottom":
            setRoomLight(master, ROOM_LEDS.ENTRANCE_BOTTOM, color)

        elif room_led_id == "main_room_top":
            setRoomLight(master, ROOM_LEDS.MAIN_ROOM_TOP, color)

        elif room_led_id == "main_room_bottom":
            setRoomLight(master, ROOM_LEDS.MAIN_ROOM_BOTTOM, color)

        elif room_led_id == "engine_room":
            setRoomLight(master, ROOM_LEDS.ENGINE_ROOM, color)

        elif room_led_id == "captains_bridge":
            setRoomLight(master, ROOM_LEDS.CAPTAINTS_BRIDGE, color)

        else:
            print("Error in set_room_light in quest_room: unknown room led {}".format(room_led_id))

    def button_pressed(self, button_id):
        self.game_state.state['pressed_buttons'].append(button_id)
        print(self.game_state.state)

    def play_robot(self, sound):
        self.sound_manager.play_sound(sound)


