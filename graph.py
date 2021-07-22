import matplotlib.pyplot as plt
import numpy as np
import wave
import os
import pydub
from SnaptoCursor import *


# utility to convert the mp3's to wav
def mp3_to_wav(p):
    s = pydub.AudioSegment.from_mp3(p)
    s.export(p.replace("mp3", "wav"), format="wav")


wav = wave.open(os.getcwd()+"\\test.wav", "r")
# wav files are BIG, so we'll downsample it later
downsample = 1000


# get raw data from wav
signal = wav.readframes(-1)
signal = np.frombuffer(signal, np.int32)
framerate = wav.getframerate()


# downsample now and get time of audio
signal = signal[::downsample]
timeline = np.linspace(0, len(signal) / framerate, num=len(signal))


# set up the graph
plt.rcParams['toolbar'] = 'None'
f, a = plt.subplots(1)
a.plot(timeline, signal)

# https://matplotlib.org/3.2.2/gallery/misc/cursor_demo_sgskip.html
snap_cursor = SnaptoCursor(a, timeline, signal, np, downsample)
f.canvas.mpl_connect('button_press_event', snap_cursor.mouse_move)


# show everything and wait for exit
plt.title("Bruh")
plt.axis('off')
plt.show()