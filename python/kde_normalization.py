#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from multivariate_kde import multi_kde
from gaussian_2d import gaussian_2d

p = gaussian_2d()

# Parameters:
sigma = 1.0

dist = np.load("dist_2d.npz")

x = dist[:,0]
y = dist[:,1]

nsamples = len(dist)

x_min = np.min(x)
x_max = np.max(x)
y_min = np.min(y)
y_max = np.max(y)

sigma_x = np.std(x)
sigma_y = np.std(y)

x_lim_pos = x_max + sigma_x
x_lim_neg = x_min - sigma_x
y_lim_pos = y_max + sigma_y
y_lim_neg = y_min - sigma_y

x_range = x_lim_pos - x_lim_neg
y_range = y_lim_pos - y_lim_neg

mesh_size = 100

x_mesh = np.linspace(x_lim_neg, x_lim_pos, mesh_size)
y_mesh = np.linspace(y_lim_neg, y_lim_pos, mesh_size)

X, Y = np.meshgrid(x_mesh,y_mesh)

Z_dat = np.zeros((mesh_size,mesh_size))

for i in range(len(x)):
    x_norm = x[i] - x_lim_neg
    y_norm = y[i] - y_lim_neg
    x_bin = int(np.round((x_norm / x_range)*mesh_size))
    y_bin = int(np.round((y_norm / y_range)*mesh_size))
    Z_dat[x_bin,y_bin] += 1
plt.contourf(X,Y,Z_dat,50,cmap='viridis')
plt.show()
bandwidths = [0.1,0.2,0.3]

# gauss_mesh = np.meshgrid(x_mesh, y_mesh)
# gauss = np.zeros((len(x_mesh),len(y_mesh)))
# for i in range(len(x_mesh)):
#     for j in range(len(y_mesh)):
#         gauss[i,j] = p(x_mesh[i],y_mesh[j])
#
# plt.contourf(X, Y, gauss, 50, cmap='viridis')
# plt.show()
#  
# print("Integral over probability KDE function:", np.sum(gauss) / nsamples * (mesh_size ** 2))
# print("Entropy using Monte Carlo:", np.sum(-gauss * np.log(gauss)) / nsamples * (mesh_size ** 2))

for bandwidth in bandwidths:
    kde = multi_kde(dist,bandwidth)

    H = kde(x_mesh,y_mesh)
    # np.savez("500x500_kde_tricky",H)

    plt.contourf(X, Y, H, 50, cmap='viridis')
    plt.show()

# Monte Carlo integration:
# x = np.random.rand(nsamples) * L - vmin
# y = np.random.rand(nsamples) * L - vmin
#
# rand_data = np.stack((np.array(x),np.array(y)), axis=1)
#
# kde = multi_kde(rand_data)
#
# #adding a small value to distribution
# g = kde(x_mesh,y_mesh)

    H += 1e-20
#
# plt.contourf(X, Y, g, 50, cmap='viridis')
# plt.show()

    # print("Integral over probability KDE function:", np.sum(H) / nsamples * (mesh_size ** 2))
    print("Entropy using Monte Carlo:", np.sum(H * np.log(H)) /  mesh_size ** 2)

