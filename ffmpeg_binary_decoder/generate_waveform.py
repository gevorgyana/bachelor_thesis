import numpy as np
import wave
import sys

from pydub import AudioSegment

sound = AudioSegment.from_mp3("sound.mp3")
sound.export("sound.wav", format="wav")
spf = wave.open("sound.wav", "r")
signal = spf.readframes(-1)
signal = np.frombuffer(signal, "int16")
