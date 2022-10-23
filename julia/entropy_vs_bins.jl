include("entropy_2d_revised.jl")
include("entropy_1d.jl")

#This function plots the entropy calculated by "entropy.jl" using different bin sizes
#Start: starting bin count, Stop: bin count stop point, Count: number of points on graph

function entropy_vs_bins(x,y,start,stop,count)
  interval = LinRange(start,stop,count)
  print(interval)
  interval = Int.(floor.(interval))
  ent = zeros(count)
  for i in 1:length(interval)
    ent[i] = entropy_2d(x , y, interval[i], interval[i])
    #ent[i] = entropy_1d(x, interval[i])
  end
  a = zeros(length(interval)) .+ 1.4189385
  graph = scatter(interval,ent, title = "Entropy vs. Bin Count")
  plot!(interval, a)
  xlabel!("Bin Count")
  ylabel!("Entropy")
  return(graph)
end
