#!/usr/bin/env python
import numpy as np
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import configparser

config = configparser.ConfigParser()

dirs = os.listdir() 

# for direc in dirs:
#     config.read(direc + "/run.param")
#     T = float(config['input']['T'])
#
    # df = pd.read_csv(direc + '/log.csv')
    # plt.plot(df['val_loss'],label=T)

df = pd.read_csv('log.csv')
plt.plot(df['val_loss'])


plt.legend()
plt.show()
