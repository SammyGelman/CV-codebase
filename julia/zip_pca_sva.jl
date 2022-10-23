#!/usr/bin/env julia
include("metropolis_2d.jl")
include("rotated_gaussian.jl")
include("product_distribution_entropy.jl")
include("covariance_matrix.jl")
include("tricky_gaussian.jl")

using NPZ
import Statistics
using LinearAlgebra


N = 50 
jump = 1000
rot_ent = zeros((N+1,2))
p = rotated_gaussian(pi)

trick_ent = zeros((N+1,2))
bins = 5000
g = tricky_gaussian() 

for i=1:N
    #get distribution
    dist = metropolis_2d(p, 0.0, 1.0, 0.0, 1.0, (i*jump), 3)

    #break apart coordinates 
    x = dist[:,1]
    y = dist[:,2]

    #find the respective covariance matrix and it's eigenvectors
    cov_mat = covariance(x,y)
    eigenvectors = eigvecs(cov_mat)

    #Transform distribution to new coordinate system
    trans_dist = dist*eigenvectors
    #counter
    count = i*jump 
    #take entropy calculation
    rot_ent[i,2] = 100*entropy(trans_dist,bins)
    rot_ent[i,1] = count
end

for i=1:N
    #get distribution
    dist = metropolis_2d(g, 0.0, 1.0, 0.0, 1.0, (i*jump), 3)

    #break apart coordinates 
    x = dist[:,1]
    y = dist[:,2]

    #find the respective covariance matrix and it's eigenvectors
    cov_mat = covariance(x,y)
    eigenvectors = eigvecs(cov_mat)

    #Transform distribution to new coordinate system
    trans_dist = dist*eigenvectors
    #counter
    count = i*jump 
    #take entropy calculation
    trick_ent[i,2] = 100*entropy(trans_dist,bins)
    trick_ent[i,1] = count
end


npzwrite("zip_pca_sva.npz", rot_ent)
npzwrite("zip_pca_sva_trick.npz", trick_ent)
