#!/usr/bin/env python

import preprocess

import tensorflow.keras as keras
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import json

def one_hot_labels(labels: []):
    """
    Map string labels to one-hot vectors.
    """
    sz = len(labels)
    output = {}

    # how to do it?
    for i, val in enumerate(labels):
        one_hot_i = [0 for i in range(sz)]
        one_hot_i[i] = 1
        output[val] = one_hot_i

    return output

def train_model_digits_from_wav():
    """
    Do multi-label classification
    """
    data = {}
    with open('data.json', 'r') as in_json:
        data = json.load(in_json)

    # convert to one-hot
    conversion = one_hot_labels(
        set(data['category'])
    )
    category = []
    # todo itertools map? :D
    for i in data['category']:
        category.append(conversion[i])
    category = np.array(category)
    print(category)

    data['mfcc'] = np.array(data['mfcc'], dtype = np.float32)

    # 10 digits
    assert data['mfcc'].shape[0] == 10 * preprocess.THRESHOLD
    # we need the most informative features we can get, 40 is the maximum
    # value for librosa.feature.mfcc
    assert data['mfcc'].shape[1] == 40
    # the next dimension can vary, depending on how fine grained
    # short FFT was.

    # Now train a simple model
    inputs = keras.Input(shape = (data['mfcc'].shape[1],
                                  data['mfcc'].shape[2]))
    layer = keras.layers.Dense(32, activation = 'softmax') (inputs)
    model = keras.Model(inputs = inputs, outputs = layer)
    model.summary()
    model.compile()
    model.fit(
        data['mfcc'], category
    )

train_model_digits_from_wav()
