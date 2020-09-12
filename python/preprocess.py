#!/usr/bin/env python

import librosa, librosa.display
import matplotlib.pyplot as plt

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

import os
import json

THRESHOLD = 1

def prepare_data():
    data = {
        'id': [],
        'mfcc': [],
        'category': [],
    }

    for i, (path, dirs, files) in enumerate(os.walk('./data')):
        category = path.split('/')[-1]
        if category in [
                'zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine',
        ]:
            print('processing {}'.format(category))
            counter = 0
            for file_name in files:

                if counter > THRESHOLD:
                    break

                counter += 1

                print("processing {}".format(file_name))
                data['id'].append(file_name)
                data['category'].append(category)
                data['mfcc'].append(
                    mel_spectrogram(
                        "{}/{}".format(
                            path, file_name
                        )
                    ).tolist()
                )

    with open('data.json', 'w') as out:
        json.dump(data, out)

prepare_data()
