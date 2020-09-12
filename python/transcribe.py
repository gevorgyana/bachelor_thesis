#!/usr/bin/env python

import librosa, librosa.display
import matplotlib.pyplot as plt

# To recognize speech, we need the words that are in the alphabet of the
# language. We donwload a sample dataset from here:
# download.tensorflow.org/data/speech_commands_v0.01.tar.gz
# and inflate it into the data/ directory.
# This dataset contains simple words like 'cat', 'dog', etc., spoken by
# native speakers. We can construct a grammar from this simple set of
# words that would correspond to the grammar of Python, for example, or
# its small subset.

def mel_spectrogram(path: str):
    # at the default sample rate = 22050 HZ
    sound_wave, sr = librosa.load(path)
    return librosa.feature.mfcc(
        sound_wave,
        sr,
        n_mfcc = 40
    )

# display a sample plot
'''
spectrogram = mel_spectrogram(
    './data/bed/00176480_nohash_0.wav'
)

librosa.display.specshow(
    spectrogram
)
plt.show()
'''

# define the grammar for the simple language, this language will recognize
# arithmetic expressions. We only have the following words in our
# alphabet:

# digits:
# zero one two three four five six seven eight nine
# other(animals):
# cat dog bird
# control commands
# off/on, up/down, stop/go, yes/no, left, right
# everything else is discarded
