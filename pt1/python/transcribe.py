#!/usr/bin/env python

import preprocess

import tensorflow.keras as keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import librosa.display
import numpy as np
import json
import functools
import itertools

import pickle

def one_hot_labels(labels: []):
    """
    Map string labels to one-hot vectors.
    """
    sz = len(labels)
    output = {}

    for i, val in enumerate(labels):
        one_hot_i = [0 for i in range(sz)]
        one_hot_i[i] = 1
        output[val] = one_hot_i

    with open('.pickle', 'wb') as pick:
        pickle.dump(
            output,
            pick
        )

    return output

def train_model_digits_from_wav():
    NUM_CLASSES = 10
    NUM_EPOCHS = 50
    """
    Do multi-label classification
    """
    # --- Prepare data
    data = {}
    with open('data.json', 'r') as in_json:
        data = json.load(in_json)

    # Convert to one-hot
    conversion = one_hot_labels(set(data['category']))

    category = []
    for i in data['category']:
        category.append(conversion[i])
    category = np.array(category)
    data['mfcc'] = np.array(data['mfcc'], dtype = np.float32)

    bad_input = 0
    with open('.badinput', 'r') as in_:
        bad_input = int(in_.readline())

    # Dimensionality checks to find bugs
    assert data['mfcc'].shape[0] == NUM_CLASSES * preprocess.THRESHOLD - bad_input
    # No empty dataset
    assert NUM_CLASSES * preprocess.THRESHOLD - bad_input != 0

    print("!!!!! shape {}".format(data['mfcc'].shape))

    # 40 is the maximum value for librosa.feature.mfcc
    assert data['mfcc'].shape[1] == 40
    # The other dimension can vary, depending on how fine-grained
    # SFFT was.

    # FEATURE: There is no way to do cross-validation out of the box
    data_train, data_test, category_train, category_test = train_test_split (data['mfcc'], category, test_size = 0.3)

    # --- Build a simple model
    inputs = keras.layers.Input(
        shape = (data['mfcc'].shape[1], data['mfcc'].shape[2])
    )
    layer = keras.layers.Flatten() (inputs)
    layer = keras.layers.Dense(32, activation = 'relu') (layer)
    layer = keras.layers.Dense(
        NUM_CLASSES, activation = 'softmax') (layer)
    model = keras.Model(inputs = inputs, outputs = layer)

    # --- Train a simple model
    model.compile(loss = 'categorical_crossentropy')
    model.summary()
    learning_history = model.fit(data_train, category_train,
              validation_data = (data_test, category_test),
              epochs = NUM_EPOCHS
    )

    model.save('tf_model')

train_model_digits_from_wav()
