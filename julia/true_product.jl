#!/usr/bin/env julia
include("metropolis_2d.jl")
include("tricky_gaussian.jl")

using NPZ

#set imported function as distribution
p = tricky_gaussian()

#generate data set
dist_2d = metropolis_2d(p, 0.0, 1.0, 0.0, 1.0, 500000, 3)

#break apart distribution into two seperate data sets
x = dist_2d[:,1]
y = dist_2d[:,2]

#move to python to visualize data
npzwrite("true_product.npz", dist_2d)
