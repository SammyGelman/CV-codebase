#!/usr/bin/env julia
using VectorizedRoutines
using Plots
using NPZ

#paramaters
sigma = 1.0
vmin = -20
vmax = 20
nsamples = 100000

function gaussian(x)
    return((1/(2*pi*sigma))*exp(-0.5*(x/sigma)^2))
end

function gaussian_2d(x,y)
    return gaussian(x) * gaussian(y)
end

x = LinRange(-10,10,100)
y = LinRange(-10,10,100)

#X, Y = Matlab.meshgrid(x,y)

#H = gaussian_2d.(X,Y)

#npzwrite("gaussian_2d_contour.npz",H)

L = vmax - vmin
x = rand(nsamples) * L + vmin 
y = rand(nsamples) * L + vmin

integration = sum(gaussian_2d.(x,y)) / nsamples * L^2

print(integration)
