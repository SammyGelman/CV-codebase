#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    exit(1)

data = np.load(sys.argv[1])
n = 100
sn = int(np.sqrt(n))
data_n = []

# for i in data.files[1:n]:
#     data_n.append(data[i])
#
fig, ax = plt.subplots(sn, sn, sharex=True, sharey=True, subplot_kw={'xticks': [], 'yticks': []})

for i,(l, s) in enumerate(data.items()):
    if i == n:
        break
    else:
        x = i // sn
        # print(x)
        y = i % sn
        # print(y)
        ax[x, y].imshow(s, aspect='auto', vmin=-1, vmax=1)


plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig("samples.pdf")
plt.show()
