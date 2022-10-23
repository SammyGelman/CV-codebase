#!/usr/bin/env julia
using NPZ
using ArgParse

include("entropy_2d_calculator.jl")

function entropy_parse()    
    s = ArgParseSettings()    
    @add_arg_table! s begin 
    "n_bins"
        help = "Enter number of bins, type=Int"
        arg_type = Int             
        default=60
     "file"
        help = "Enter relevant file name."
        arg_type = String
        default="dist_2d.npz"
    end

    return parse_args(s)
end

arg = entropy_parse()

dist = npzread(arg["file"])
x = dist[:,1]
y = dist[:,2]

num_entropy = entropy_2d(x,y,arg["n_bins"],arg["n_bins"])
print("Entropy using Metropolis Algorithm of " , arg["file"],  ": " , num_entropy,"
")
