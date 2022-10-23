#!/usr/bin/env julia
include("covariance_matrix.jl")
import Statistics
using LinearAlgebra
using NPZ

#get distribution
dist = npzread("dist_2d.npz")
x = dist[:,1]
y = dist[:,2]
#return(x,y)

#find the respective covariance matrix and it's eigenvectors
cov_mat = covariance(x,y)
npzwrite("cov_mat.npz", cov_mat)
eigenvectors = eigvecs(cov_mat)

#Transform distribution to new coordinate system
trans_dist = dist*eigenvectors
u = trans_dist[:,1]
v = trans_dist[:,2]
npzwrite("trans_dist.npz", trans_dist)
#second = histogram2d(u,v, bins=200)

#find covariance matrix and eigenvectors of in new coordinate system
trans_cov_mat = covariance(u,v)
npzwrite("trans_cov_mat.npz", trans_cov_mat)
eigenvectors2 = eigvecs(cov_mat)

