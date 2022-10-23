function entropy_2d(x, y, n_bins_x, n_bins_y)

  #Find the range of x and y
  x_max = maximum(x)
  x_min = minimum(x)
  y_max = maximum(y)
  y_min = minimum(y)

  x_range = x_max - x_min
  y_range = y_max - y_min

  #Turn x and y into the bins they will go into
  #for i in 1:length(x)
  #  x[i] = floor(x[i]/x_range*n_bins_x) + 1
  #end
  #for i in 1:length(y)
  #  y[i] = floor(y[i]/y_range*n_bins_y) + 1
  #end

  bin_x = Int.(floor.((x .- x_min)./x_range.*(n_bins_x .- 1)).+ 1)
  bin_y = Int.(floor.((y .- y_min)./y_range.*(n_bins_y .- 1)).+ 1)

  #set matrix for entropy
  M = zeros(n_bins_x,n_bins_y)

  #place data in respective bins
  for i in 1:length(x)
    M[bin_x[i],bin_y[i]] += 1
  end
  
  #calculate the probability of landing at any index in matrix M 
  dx = x_range/n_bins_x
  dy = y_range/n_bins_y

  M = M ./ sum(M) / (dx*dy)
  M = M .+ 10^(-20)

  #calculate the entropy of the system
  entropy = -sum(log.(M).*M)*(dx*dy)
  return(entropy)

end
