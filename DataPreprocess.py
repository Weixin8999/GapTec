#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:16:06 2019

@author: yudiwang
"""
# In[]
import librosa
#import IPython.display as ipd
#import matplotlib.pyplot as plt
import pandas as pd
import librosa.display
import numpy as np
import sklearn
#import ctypes
import os 
import os.path
#import sys
# In[]
numDirs = 0
types = []
path = "/Users/yudiwang/Documents/19Winter ECE 271B/Group Project/dataSet"
for dirpath, dirnames, filenames in os.walk(path):
        for name in dirnames:
                types.append(os.path.join(dirpath, name))
                numDirs += 1
                print (os.path.join(dirpath, name))
                
numFiles = []
names = [[],[],[],[],[],[],[]]
for i in range(numDirs):
    path = types[i]
    for dirpath, dirnames, filenames in os.walk(path):
        numType = 0
        for each in filenames:
            names[i].append(os.path.join(dirpath, each))
            numType += 1
        numFiles.append(numType)

trainLabels = []
for i in range(numDirs):
    for j in range(numFiles[i]):
        trainLabels.append(i)

# In[]
from numpy import ndarray
#import random

trainSounds = []
for i in range(numDirs):
    for j in range(numFiles[i]):
        path = names[i][j]
        y, sr = librosa.load(path, sr = 44100)
        audio_mfcc = librosa.feature.mfcc(y=y, sr = sr, n_mfcc = 20)
        mfcc_flat = ndarray.flatten(audio_mfcc) 
        trainSounds.append(mfcc_flat)
    
trainSounds = np.asarray(trainSounds)
trainLabels = np.asarray(trainLabels)
#Sound_Label = [trainSounds, trainLabels]
# In[]
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

shuffle_sounds, shuffle_labels=unison_shuffled_copies(trainSounds, trainLabels)

train_sound = shuffle_sounds[0:6115]
test_sound = shuffle_sounds[6115:]

train_labels = shuffle_labels[0:6115]
test_labels = shuffle_labels[6115:]

train_sound_file = pd.DataFrame(data = train_sound)
train_sound_file.to_csv('train_sound_data.csv',encoding='utf-8')

train_labels_file = pd.DataFrame(data = train_labels)
train_labels_file.to_csv('train_label_data.csv',encoding='utf-8')

test_sound_file = pd.DataFrame(data = test_sound)
test_sound_file.to_csv('test_sound_data.csv',encoding='utf-8')

test_labels_file = pd.DataFrame(data = test_labels)
test_labels_file.to_csv('test_labels_data.csv',encoding='utf-8')

