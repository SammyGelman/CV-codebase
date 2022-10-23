#!/usr/bin/env julia
include("metropolis_1d.jl")
using NPZ

#get one dimensional gaussian distribution
function distribution(mu=0.0, sigma=1.0)
  function p(x)
		gaussian = (1/(sigma*2*pi)^0.5)*exp(-((x-mu)^2)/(2*sigma))
  end
end

#compute
dist = metropolis_1d(distribution(), 0.0, 0.5, 20000000, 10)
npzwrite("dist.npz", dist)
