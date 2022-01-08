#!/usr/bin/env python3
#coding=utf-8
import os,sys
from threading import active_count

from numpy.core.fromnumeric import transpose
os.chdir(sys.path[0])

import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import ast

### 1)加载数据
def load_data():
    df = pd.read_csv('./iiwa_dataset.csv')
    train_set = df.head(6000)
    test_set = df.tail(df.shape[0]-6000)
    
    train_datas = [];train_labels = []
    for rows in train_set.itertuples():
        _labels = ast.literal_eval(rows.Joint)
        _datas = ast.literal_eval(rows.Pose)
        train_datas.append(np.array(_datas).reshape(21,))
        train_labels.append(np.array(_labels).reshape(7,))
    
    train_datas = np.array(train_datas)
    train_labels = np.array(train_labels)
    return train_labels,train_datas
    
### 2)搭建网络
class IIWA_NN:
    
    def __init__(self):
        self.__model = keras.Sequential([
            keras.layers.Flatten(input_shape=(1,21)),
            keras.layers.Dense(100,activation='relu'),
            keras.layers.Dense(100,activation='relu'),
            keras.layers.Dense(100,activation='relu'),
            keras.layers.Dense(100,activation='relu'),
            keras.layers.Dense(100,activation='relu'),
            keras.layers.Dense(7)
        ])
        self.__model.summary()

### 3)对数据进行正则化
def data_normal(labels,datas):
    print()
    pass


if __name__ == "__main__":
    train_labels,train_datas = load_data()
    iiwa_nn = IIWA_NN()