#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Global:
    SCENARY_FILE = "./full_quest.yml"
    GET_TTY_USB_SCRIPT = "./get_ttyUSB.sh "
    INIT_TASK_ID = 0
    RAVEN_DNS = ("https://4c6ae2fddd3d4e8db0d5c48987713a46:"
        "cfef5efe75c54965878647629f3180a6@sentry.io/181588")


class Devices:
    DEVICE = "DEVICE"
    LOVECRAFT_DEVICE_NAME = "LOVECRAFT_DEVICE_NAME"
    LOVECRAFT_USB_SERIAL_NUMBER = "AL0079C6"
    LOVECRAFT_DEVICE_COM_PORT_WIN = "COM3"


class COLORS:
    FISH_NORMAL = [0x02, 0x02, 0x02]
    FISH_LIGHTNING = [0x100, 0x00, 0x00]

    WHITE = [0xff, 0xff, 0xff]
    RED = [0xff, 0, 0]
    LIGHT_RED = [0xff, 33, 33]
    GREEN = [0, 0xff, 0]
    LIGHT_GREEN = [33, 0xff, 33]
    BLUE = [0, 0, 0xfff]
    NONE = [0, 0, 0]
    OFF = NONE
    # for ROOMS it's RGB => BGR
    ROOM_BLUE = [BLUE[2], BLUE[1], BLUE[0]]
    ROOM_RED = [RED[2], RED[1], RED[0]]
    ROOM_GREEN = [GREEN[2], GREEN[1], GREEN[0]]


class DEVICES_TABLE:

    # ADC
    ADC_LORDS_TABLE_STATUE = 0
    LORDS_TABLE_STATUE_RANGE = (113, 115)
    LORDS_TABLE_STATUE_NONE_RANGE = (110, 150)

    BOX_LOCK_SYMBOL_1 = 6
    BOX_LOCK_SYMBOL_2 = 5
    BOX_LOCK_SYMBOL_3 = 7
    SYMBOL_1_VALUE_RANGE = (29, 66)
    SYMBOL_2_VALUE_RANGE = (0, 5)
    SYMBOL_3_VALUE_RANGE = (180, 190)

    COIN_1 = 1
    COIN_2 = 2
    COIN_3 = 3
    COIN_4 = 4
    COIN_INSERTED_RANGE = (30, 36)
    COIN_NONE_RANGE = (37, 130)

    # RELAY
    RELAY_CLOSET_DOOR_1 = 0
    RELAY_CLOSET_DOOR_WITH_SKELET = 1
    RELAY_GODS_TABLE_MOTOR = 2
    RELAY_PUSH = 3
    # relay actions
    RELAY_CLOSE = 1
    RELAY_OPEN = 0

    # Btn
    BTN_COLLECT_DAD_FISHING = 1
    BTN_PICTURE_BARLEY_BREAK = 17
    BTN_CODE_LOCKS_CODE_BUTTONS = 2
    BTN_CODE_LOCKS_ELSE_BUTTONS = 3

    BTN_HEAD_SENSOR = 4

    BTN_BOTTLES = 0

    BTN_KNIFE_SLOTS = [11, 10, 12, 13, 14]

    BTN_DOOR_OPEN = 15

    # SimpleLeds
    CLOSE = 1
    OPEN = 0
    SL_TABLE_CLOCK_ZERO_CMD = 0
    SL_TABLE_CLOCK_NEXT_TIME_CMD = 1
    SL_TABLE_CLOCK_RING_OUT = 20  # led7 B

    FALLING_BOOK_RODS_TIMER = 1
    SL_FISHING_RODS_HOLDERS = 14  # change from 13

    SL_WALL_CLOCK_LOCK_WITH_PICTURE = 11  # LOCK - 1
    SL_WALL_CLOCK_LOCK_WITH_COIN = 10  # LOCK - 2

    SL_SCARES_ALL = [15, 17]
    SL_SCARE_IN_LOCKER = [15, 17]

    SL_CODE_LOCKS_LOCKER_LOCK = 9

    SL_DOLL_EYES_PUMP = 3  # 2B
    DOLL_EYES_PUMP_TIME = 4
    SL_AQUARIUM_PUMP = 4
    AQUARIUM_PUMP_TIME = 30
    AQUARIUM_FILL_TIME = 2*60 + 10

    SL_BOX_IN_CLOSET_WITH_KNIFE = 12
    SL_MIRROR_IN_CLOSET = 13

    SL_BOX_UNDER_PICTURE = 5

    SL_EDDISON_LIGHT = 23

    SL_MOVING_PICTURE = [18, 21, 22, 19]

    SL_SCARE_WINDOW = 16
    SL_HEAD_WINDOW_MOTOR = 45
    SL_HEAD_WINDOW_ACTION = 46
    HEAD_ACTION_APPEAR = 0
    HEAD_ACTION_HIDE = 1

    # Encoders
    WALL_CLOCK = 2

    # Smart LEDs
    SML_FISHING_ROD = 6
    SML_STOREROOM = 6
    SML_STOREROOM_SECRET = 7
    SML_DOLL = 4

    # lightning
    SML_LIGHTNING = [16, 17]
    SML_MATRIX_SOB = 0
    SML_HALL_END = 8
    SML_HALL_BEGIN = 9
    SML_WINDOWS = 16
    SML_WINDOWS_DOUBLE_HREN = 17

    # FISH EYES
    SML_FISH_EYES = [28, 27, 26, 25, 24]

    SML_ALL_LIGHTS = [
            SML_FISHING_ROD,
            SML_STOREROOM,
            SML_STOREROOM_SECRET,
            SML_DOLL,
            SML_HALL_END,
            SML_HALL_BEGIN,
            SML_WINDOWS,
            SML_WINDOWS_DOUBLE_HREN
            ] + SML_FISH_EYES

    SML_SCARE_ALL_LIGHT = [
            SML_FISHING_ROD,
            SML_STOREROOM,
            SML_STOREROOM_SECRET,
            SML_DOLL,
            SML_HALL_END,
            SML_WINDOWS,
            SML_WINDOWS_DOUBLE_HREN
            ] + SML_FISH_EYES

    TIMER_PLAY_LIFESAVER_END = 2*60
    TIMER_PLAY_BAD_END = 60
    TIMER_PICTURE_BOX =15
    TIMER_SCARE_WINDOW = TIMER_PICTURE_BOX + 30
    TIMER_SCARE_HEAD = TIMER_PICTURE_BOX + 35
    TIMER_PLAY_BEGGINING_AFTER_MINUTE = 60
    TIMER_STOOREROOM_OPEN_DOOR = 60 + 10

class TASKS_IDS:
    INITIALIZATION = 0
    INITIALIZATION_GODS_TABLE = 101

    START_QUEST = 1000
    BACKGROUND_WALL_CLOCK_INIT = 110
    FALLING_BOOK_RODS_TIMER = 120

    PLAY_SOUND_HELP = 201
    PLAY_SOUND_BEGIN = 202
    PLAY_SOUND_BEGINNING_AFTER_MINUTE = 203
    PLAY_BEFORE_FALLING_BOOKS = 204
    PLAY_SOUND_FISHING = 205
    PLAY_SOUND_ABOUT_COINS_AND_CLOSET = 206
    PLAY_SHE_ALL_WHAT_I_HAVE = 207
    PLAY_CLOSET = 208
    PLAY_PRAY = 209
    PLAY_GIRL_YOU_HEAR_ME = 210
    PLAY_DIVISION = 211
    PLAY_DAGON_PRIVATE = 212
    PLAY_KNIFE_ACHIEVED = 213
    PLAY_OLD_MAN_MONOLOG = 214
    OPEN_STOORE_ROOM_DOOR = 215
    PLAY_AFTER_SKELET_DOOR_OPEN = 216
    PLAY_ALL_COINS_ON_PLACE = 217
    PLAY_CHEST = 218
    STOOREROOM_OPEN_DOOR_TIMER = 300

    FINAL_DAGON = 219
    PLAY_SOUND_DOLL_HELP = 220
    PLAY_SOUND_BACKGROUND_SOUND = 221
    PLAY_SOUND_ARRAY = 222;

    PUT_STATUE_ON_LORDS_TABLE = 1
    PUT_FIRST_COIN = 2
    COLLECT_DAD_FISHING = 3
    BACKGROUND_TABLE_CLOCK = 4
    CLOCK_SYNCHRONIZATION = 5
    TABLE_CLOCK_RING_OUT_ALWAYS = 112
    FAMILY_PICTURE_BARLEY_BREAK = 6
    PUT_SECOND_COIN = 7
    CODE_LOCK = 8
    ONCOMING_TO_KUNSTKAMERA = 9
    AQUARIUM_PUMP = 90
    AQUARIUM_FILL = 91
    PLACE_THE_BOTTLES = 10
    OPEN_BOX_IN_THE_PANTRY = 11

    CLOSE_THE_DOOR = 13

    PUT_THIRD_COIN = 16
    # PUT_FOURTH_COIN = 16

    ANOMALOUS_PHENOMENA_LEDS = 17
    ANOMALOUS_PHENOMENA_ENTER_NUMBERS = 18

    MARINE_TROPHIES = 19

    PUT_FOURTH_COIN = 20

    TIMER_PLAY_LIFESAVER_END = 121
    TIMER_PLAY_BAD_END = 122
    TIMER_SCARE_WINDOW = 123
    TIMER_SCARE_HEAD =124
    TIMER_PICTURE_BOX = 125

    EDDISON_LAMP_BLINK = 140

    THE_FINAL = 21


class SOUNDS_NAMES:
    SOUNDS_DIR = "./music/changed/"
    STAGE_1 = SOUNDS_DIR + "stage_one_whisper.wav"
    LIFESAVER_1 = SOUNDS_DIR + "lifesaver_2_1.wav"
    LIFESAVER_2_2 = SOUNDS_DIR + "lifesaver_2_2.wav"
    LIFESAVER_2_1 = SOUNDS_DIR + "lifesaver_2_1.wav"
    LIFESAVER_3_1 = SOUNDS_DIR + "lifesaver_3_1.wav"
    GIRL_1_HELP = SOUNDS_DIR + "girl_1_help.wav"
    GIRL_2_HEARD = SOUNDS_DIR + "girl_2_i_heard.wav"
    GIRL_4_SHE_ALL_I_HAVE = SOUNDS_DIR + "girl_4_she_all_i_have.wav"
    STAGE_2 = SOUNDS_DIR + "stage_two_call.wav"
    STAGE_3 = SOUNDS_DIR + "stage_three_shout.wav"
    STAGE_4 = SOUNDS_DIR + "stage_four_madness.wav"
    LIGHTNING = SOUNDS_DIR + "lightning_thunder.wav"

    OLD_MAN = SOUNDS_DIR + "old_man_monolog.wav"
    DAGON_PRIVATE = SOUNDS_DIR + "dagon.wav"

    BAD_END = SOUNDS_DIR + "bad_end.wav"


    PREY = SOUNDS_DIR + "prey.wav"
    NAMES = SOUNDS_DIR + "names.wav"
    PICTURE = SOUNDS_DIR + "picture.wav"
    NOT_UNDERSTAND = SOUNDS_DIR + "not_understand.wav"
    DIVISION = SOUNDS_DIR + "division.wav"
    CHEST = SOUNDS_DIR + "chest.wav"
    HE = SOUNDS_DIR + "he.wav"
    DOLL = SOUNDS_DIR + "doll.wav"

    BEGIN = SOUNDS_DIR + "begin.wav"
    MUSIC_ON_DEMON_WINGS = SOUNDS_DIR + "music_on_demon_wings.wav"
    BEGIN_MIN_LATER = SOUNDS_DIR + "begin_min_later.wav"
    FIRST_COIN = SOUNDS_DIR + "first_coin.wav"
    BEFORE_BOOKS_FALL = SOUNDS_DIR + "before_books_fall.wav"
    AFTER_BOOKS_FALL = SOUNDS_DIR + "after_books_fall.wav"
    FISHING = SOUNDS_DIR + "fishing.wav"
    CLOCK_SYNC = SOUNDS_DIR + "clock_sync.wav"
    SECOND_COIN = SOUNDS_DIR + "second_coin.wav"
    CLOSET = SOUNDS_DIR + "closet.wav"
    KNIFE_ACHIEVED  = SOUNDS_DIR + "knife_achieved.wav"
    ALL_COINS_ON_PLACE = SOUNDS_DIR + "all_coins_on_place.wav"
    AFTER_SKELET_DOOR_OPEN = SOUNDS_DIR + "after_skelet_door_open.wav"
    CTHULHU_APPEAR = SOUNDS_DIR + "cthulhu_appear.wav"
    OPERATOR_END = SOUNDS_DIR + "operator_end.wav"


    LIFESAVER_3_1_FIRST = SOUNDS_DIR + "lifesaver_3_1_first.wav"
    LIFESAVER_3_1_SECOND = SOUNDS_DIR + "lifesaver_3_1_second.wav"

    GIRL_PLEASE_STOP = SOUNDS_DIR + "girl_please_stop.wav"
    GIRL_WHO_ARE_YOU = SOUNDS_DIR + "girl_who_are_you.wav"
    GIRL_HEAR_ME = SOUNDS_DIR + "girl_hear_me.wav"

class SOUNDS:
    stage_1 = None
    lifesaver_begin = None
    lifesaver_end = None
    lightning = None
    girl_help = None
    girl_heard = None
    girl_she_all_i_have = None

    old_man = None
    dagon_private = None
    bad_end = None

    stage_2 = None
    stage_3 = None
    stage_4 = None
    stages = []


    prey = None
    names = None
    picture = None
    not_understand = None
    division = None
    chest = None
    he = None
    doll = None

    begin = None
    music_on_demon_wings = None
    begin_min_later = None
    first_coin = None
    before_books_fall = None
    after_books_fall = None
    fishing = None
    clock_sync = None
    second_coin = None
    closet = None
    knife_achieved = None
    all_coins_on_place = None
    after_skelet_door_open = None
    cthulhu_appear = None
    operator_end = None

    girl_please_stop = None
    girl_who_are_you = None
    girl_hear_me = None

    lifesaver_end_first = None
    lifesaver_end_second = None
