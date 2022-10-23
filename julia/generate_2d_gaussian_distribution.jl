#!/usr/bin/env julia
include("metropolis_2d.jl")
include("rotated_gaussian.jl")
include("symmetric_gaussian.jl")
include("tricky_gaussian.jl")

using NPZ
using ArgParse

function read_arg()    
    s = ArgParseSettings()    
    @add_arg_table! s begin 
#    "theta"
#        help = "Enter value for theta, type=float"
#        arg_type = Float64             
#        default= 3 * Float64(pi)
    "function"
        help = "For symmetric enter 'gaussian', rotated enter 'rotated' and pca four enter 'four'"
    "N"
        help = "N is number of samples for metropolis algorithm"
        arg_type = Int
        default = 500000
    end

    return parse_args(s)
end

args = read_arg()
#get two dimensional gaussian distribution
if args["function"] == "gaussian"
    p = gaussian_2d()
elseif args["function"] == "rotated"
#    p = rotated_gaussian(["theta"])
    p = rotated_gaussian(pi)
elseif args["function"] == "four"
    p = tricky_gaussian()
end

#compute
dist_2d = metropolis_2d(p, 0.0, 8.0, 0.0, 8.0, 100000, 20)
npzwrite("dist_2d.npz", dist_2d)
