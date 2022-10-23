function entropy_1d(x, n_bins_x)

  #find the range of x
  x_max = maximum(x)
  x_min = minimum(x)

  x_range = x_max - x_min

  #turn points into bin numbers
  bin_x = int.(floor.((x .- x_min)./x_range.*(n_bins_x - 1)).+ 1)

  #set vector for bins
  e = zeros(n_bins_x)

  #place data in respective bins
  for i in 1:length(x)
    e[bin_x[i]] += 1
  end

  #calculate the probability of landing at any index in vector e
  e = e ./ sum(e)
  #add a very small number to avoid error when taking the logarithm
  e = e .+ 10^(-20)

  #calculate the entropy of the system
  dx = x_range/(n_bins_x-1)
  entropy = -sum(log.(e).*e)*dx
  return(entropy)
end
