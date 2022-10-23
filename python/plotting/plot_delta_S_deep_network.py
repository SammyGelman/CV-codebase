#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import re
import os
from scipy import interpolate
from figures import *
from onsager_solution import onsager_entropy
import glob
from exact_solution import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('parameter', type=str, nargs='+',
                    help='directory catch dup values')

args = parser.parse_args()
parameter = args.parameter[0]

if parameter == 'training_samples':
    param = ['10000','20000','40000','80000','160000','320000']
elif parameter == 'drop_out':
    param = ['0.3','0.4','0.5','0.6','0.7']
elif parameter == 'batch_size':
    param = ['32','64','128','256','512']
elif parameter == 'filters':
    param = ['32','64','128','256']
elif parameter == 'logistic_mix':
    param = ['2','4','6','8','10']
elif parameter == 'num_resnet':
    param = ['2','4','6','8']
#create fig
fig = create_figure()
ax = create_single_panel(fig,xlabel=parameter,ylabel="Delta S")

dirs = next(os.walk('.'))[1]

S_dict=np.zeros((len(dirs),2))
std_err=np.zeros((len(dirs),2))
delta_S=np.zeros((len(dirs),2))

T = 2.269183
l = 16

i = 0
for s in param:
    entropy_filename = 'final_entropy_'+str(s)+'.txt'
    if os.path.isfile(entropy_filename):
        # data = np.loadtxt(entropy_filename)[-1:]
        data = np.loadtxt(entropy_filename)
        print("number of entropy data point for training samples " + str(s) + ": ", len(data))
        avg_ent = np.mean(data)
        S_dict[i] = np.array(s,avg_ent)
        std_err[i] = np.array((s, (np.std(data)/np.sqrt(len(data)))))
        S_exact = S(T,l)
        dS = avg_ent - float(S_exact)
        delta_S[i] = np.array((s, dS))
    i+=1

ds_sorted = sorted(delta_S, key=lambda x:x[0])
error_sorted = sorted(std_err, key=lambda x:x[0])

t_s = []
d_s = []
std = []

for ds in ds_sorted:
    t_s.append(ds[0])
    d_s.append(ds[1])

print(d_s)

for err in error_sorted:
    std.append(err[1])

print(std)
# Plot and output entropy difference
ax.errorbar(t_s, d_s, std)
ax.axhline(y=0.0002)

np.savetxt('std.dat', std)
np.savetxt('delta_S.dat', ds_sorted)

finalize_and_save(fig, 'exact_temperature_entropy.pdf')
plt.show()
