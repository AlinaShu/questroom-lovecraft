import pyaudio
import wave
import time
import sys
import numpy
from fractions import Fraction
import threading

from wavefile import WaveReader

def run_in_thread(fn):
    def run(*k, **kw):
        t = threading.Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

class Sound:
    CHUNK = 512

    def __init__(self, sound_name):
        self.sound_name = sound_name
        self.sound_file = WaveReader(sound_name)
        self.channels = self.sound_file.channels
        self.player_lib = pyaudio.PyAudio()
        self._volume = 1


        # self.wf = wave.open(sound_name, 'rb')
        # self.p = pyaudio.PyAudio()
        # self.device_index, self.max_channels = self.get_valid_device_info(self.p)


    def callback(self, in_data, frame_count, time_info, status):
        # data = self.wf.readframes(frame_count)
        # numpy_array = numpy.fromstring(data, 'int16') * self._volume
        # new_data = numpy_array.astype('int16').tostring()
        data = self.sound_file.buffer(512)
        nframes = self.sound_file.read(data)
        new_data = data[:, :nframes]

        # new_data = self.sound_file.read(frame_count)

        # new_data = self.sound_file.read_iter(size=frame_count)
        # new_data = self.sound_file.read(frame_count)
        return (new_data, pyaudio.paContinue)


    def open_stream(self):
        # stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
        #     channels=min(self.wf.getnchannels(), self.max_channels),
        #     output_device_index=1,
        #     rate=self.wf.getframerate(),
        #     output=True)
        # return stream
        #
        stream = self.player_lib.open(
            format = pyaudio.paFloat32,
            channels = self.channels,
            rate = self.sound_file.samplerate,
            frames_per_buffer = 512,
            output=True,
            stream_callback=self.callback)
        return stream

    @run_in_thread
    def play(self, repeat_count = 1):
        stream = self.open_stream()
        stream.start_stream()
        print("File: {} playing\n".format(self.sound_name))
        # while stream.is_active():
        #     time.sleep(0.1)
        #     sys.stdout.write("."); sys.stdout.flush()
        # stream.stop_stream()
        # stream.close()
        # self.sound_file.close()
        # self.player_lib.terminate()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self._volume_fraction = Fraction(self._volume).limit_denominator()

