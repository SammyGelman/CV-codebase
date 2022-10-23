#!/usr/bin/env julia
using NPZ
using ArgParse

function read_arg()    
    s = ArgParseSettings()    
    @add_arg_table! s begin 
    "file"
        help = "Enter file name of distribution."
        arg_type = String             
    "nbins"
        help = "Enter the number of bins desired for numeric entropy calculation"
        arg_type = Int
    end

    return parse_args(s)
end

#args = read_arg()

#dist = npzread(args["file"])
#nbins = args["nbins"]

function entropy(dist, nbins)
    ent = []    
    
    for i in 1:length(dist[1,:])
        
        x = dist[:,i]

        #find the range of x
        x_max = maximum(x)
        x_min = minimum(x)

        x_range = x_max - x_min

        #turn points into bin numbers
        bin_x = Int.(floor.((x .- x_min)./x_range.*(nbins - 1)).+ 1)

        #set vector for bins
        e = zeros(nbins)

        #place data in respective bins
        for i in 1:length(x)
            e[bin_x[i]] += 1
        end

        #calculate the probability of landing at any index in vector e
        e = e ./ sum(e)
        #add a very small number to avoid error when taking the logarithm
        e = e .+ 10^(-20)

        #calculate the entropy of the system
        dx = x_range/(nbins-1)
        append!(ent, -sum(log.(e).*e)*dx)
    end
    return(sum(ent))
end

#val = entropy(dist, nbins)

print("Entropy assuming is a product distribution: ", val)
