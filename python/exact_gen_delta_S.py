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

#collect directories
def get_temp(s):
    m = re.search(r'T(.*?)_', s)
    return float(m.group(1))

#create fig
fig = create_figure()
ax = create_horizontal_split(fig,2,merged=False,xlabel="Temperature",ylabel="Entropy")

S_dict={}
std_err={}

dirs = next(os.walk('.'))[1]
dirnames = glob.iglob('T*')

for dirname in dirnames:
    config.read(str(dirname) + "/run.param")
    n = int(config['input']['l'])
    
    entropy_filename = str(dirname) + '/final_entropy.txt'
    # print("Trying " + entropy_filename + "...")
    if os.path.isfile(entropy_filename):
        # data = np.loadtxt(entropy_filename)[-1:]
        data = np.loadtxt(entropy_filename)
        T = get_temp(entropy_filename)
        S_dict[T] = np.mean(data)
        std_err[T] = np.std(data)
# Get sorted data
data_T = np.array(list(sorted(S_dict.keys())))
data_S = np.array(list(map(lambda T: S_dict[T], data_T)))
data_std_err = np.array(list(map(lambda T: std_err[T], data_T)))

# Get analytical entropy
T_smooth = np.linspace(0.05, 15, 1500)
S_exact = np.zeros(len(T_smooth))

for t_n in range(len(T_smooth)):
    S_exact[t_n] = S(T_smooth[t_n], n)

onsager_S_data_T = np.array(list(map(onsager_entropy, data_T)))
S_exact_data_T = np.zeros(len(data_T))

for t_n in range(len(data_T)):
    S_exact_data_T[t_n] = S(data_T[t_n], n)

delta_S = data_S - S_exact_data_T

# Save results
np.savetxt('S.dat', np.c_[data_T, data_S])
np.savetxt('error.dat', np.c_[data_T, data_std_err])
np.savetxt('delta_S_exact.dat', np.c_[data_T, delta_S])
np.savetxt('exact_S.dat', np.c_[T_smooth, S_exact])

# Plot entropies
ax[0].plot(T_smooth, S_exact)
ax[0].scatter(data_T, data_S)
ax[0].errorbar(data_T, data_S, yerr=data_std_err, fmt=' ')

# Plot and output entropy difference
ax[1].plot(data_T, delta_S)

finalize_and_save(fig, 'exact_temperature_entropy.pdf')
plt.show()
