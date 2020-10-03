#!/usr/bin/env python

import preprocess
import numpy as np
import librosa
import matplotlib.pyplot as plt
import pickle
from tensorflow import keras

def run():
    one = preprocess.mel_spectrogram(
        'evaluation/one/out.wav'
    ).tolist()
    one = np.array(one, dtype = np.float32)
    # librosa.display.specshow(
    #    one
    # )
    # plt.show()
    one = np.reshape(
        one,
        (1, 40, 44)
    )
    print(one.shape)

    model = keras.models.load_model('tf_model')
    res = model.predict(one).tolist()
    res = np.reshape(res, (len(res[0])))
    with open('.pickle', 'rb') as pck:
        conv = pickle.load(pck)
    rev_conv = {}
    cnt = 0
    for i in conv.keys():
        value = conv[i]
        rev_conv[cnt] = i
        cnt += 1

    for ith, i in enumerate(res):
        if i < 0.1:
            continue
        print("{} : {}".format(rev_conv[ith], i))

if __name__ == '__main__':
    run()
