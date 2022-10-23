#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import re
import os
from scipy import interpolate
import configparser
from figures import *
from onsager_solution import onsager_entropy
import glob
from exact_solution import *

config = configparser.ConfigParser()
config.optionxform = str

#create fig
fig = create_figure()
ax = create_single_panel(fig,xlabel="Training Samples",ylabel="Delta S")

dirs = next(os.walk('.'))[1]

S_dict=np.zeros((len(dirs),2))
std_err=np.zeros((len(dirs),2))
delta_S=np.zeros((len(dirs),2))

i = 0
for dirname in dirs:
    config.read(str(dirname) + "/run.param")
    ts = int(config['input']['training_samples'])
    n = int(config['input']['l'])
    T = float(config['input']['T'])
    
    entropy_filename = str(dirname) + '/final_entropy.txt'
    # print("Trying " + entropy_filename + "...")
    if os.path.isfile(entropy_filename):
        # data = np.loadtxt(entropy_filename)[-1:]
        data = np.loadtxt(entropy_filename)
        print("number of entropy data point: ", len(data))
        avg_ent = np.mean(data)
        S_dict[i] = np.array(ts,avg_ent)
        std_err[i] = np.array((ts, (np.std(data)/np.sqrt(len(data)))))
        S_exact = S(T,n)
        dS = avg_ent - float(S_exact)
        delta_S[i] = np.array((ts, dS))
    i+=1
# Save results
# np.savetxt('S.dat', np.c_[data_T, data_S])
# np.savetxt('error.dat', np.c_[data_T, data_std_err])
# np.savetxt('delta_S_exact.dat', np.c_[data_T, delta_S])
# np.savetxt('exact_S.dat', np.c_[T_smooth, S_exact])

ds_sorted = sorted(delta_S, key=lambda x:x[0])
error_sorted = sorted(std_err, key=lambda x:x[0])
print(ds_sorted)
t_s = []
d_s = []
std = []

for ds in ds_sorted:
    t_s.append(ds[0])
    d_s.append(ds[1])

for err in error_sorted:
    std.append(err[1])

print(std)
# Plot and output entropy difference
ax.errorbar(t_s, d_s, std)
ax.axhline(y=0.0002)
#
np.savetxt('std.dat', std)
np.savetxt('delta_S.dat', ds_sorted)

finalize_and_save(fig, 'exact_temperature_entropy.pdf')
plt.show()
