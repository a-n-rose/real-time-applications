'''
Real-time audio functionality in Python using SoundCard
implementing selective filtering - version 1
Version 1:
+ works in real-time 
+ can record specific sounds to filter out
+ can adjust strength of filter (not real-time though)
- latency is around 2 seconds
- musical noise is still quite bad
- Wiener filter is not yet implemented
- no downsampling or upsampling
'''

import sys

import numpy as np
import soundcard as sc

import numpy as np
import sounddevice as sd
import soundfile as sf
import librosa

import prep_noise as pn


def record(duration,fs,channels):
    print("Recording noise for {} seconds...".format(duration))
    sound = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    return sound

sr = 22000 #sampling rate
strength = 0.5 #filter strength

print("Press ENTER to record the noise you want to filter out:")
rec = input()
if rec == "":
    noise = record(5,sr,1)
else:
    sys.exit()
    

# get a list of all speakers:
speakers = sc.all_speakers()
# get the current default speaker on your system:
default_speaker = sc.default_speaker()
# get a list of all microphones:
mics = sc.all_microphones()
# get the current default microphone on your system:
default_mic = sc.default_microphone()


noise = noise.reshape((noise.shape[0]))
#to make this faster, perhaps downsample to 16 or 8 kHz and then upsample to 48 again
with default_mic.recorder(samplerate=sr,channels=1) as mic, \
      default_speaker.player(samplerate=sr) as sp:
    for _ in range(1000):
        data = mic.record(numframes=1024)
        data = data.reshape((data.shape[0]))
        data_nr = pn.rednoise(data,noise,sr,strength)
        data_nr = data_nr.reshape(data_nr.shape+(1,))
        sp.play(data_nr)
