#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import configparser
from sys import argv

# dirs = argv[1:]
#
# config = configparser.ConfigParser()
# dir = sorted(dirs)
#
# for direc in dirs:
#     config.read(str(direc)+"/run.param")
#     T = float(config['input']['T'])
#     loss = np.loadtxt(str(direc)+'/loss.dat')
#     plt.plot(loss[:,0],loss[:,1],label=str(T))
#     # plt.plot(loss[0,:],loss[1,:],label=str(T))
#     plt.legend()
#
# plt.show()

loss = np.loadtxt('loss.dat')
val_loss = np.loadtxt('validation_loss.dat')
plt.plot(loss[:,0],loss[:,1],label='loss')
plt.plot(val_loss[:,0],val_loss[:,1],label='val_loss')
plt.show()
