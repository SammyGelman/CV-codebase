function covariance(x,y)
     len = length(x)
     mean_x = sum(x)/len
     mean_y = sum(y)/len
#mean normalization first!
    x_norm = (x.-mean_x)./(maximum(x)-minimum(x))
    y_norm = (y.-mean_y)./(maximum(y)-minimum(y))
    X = [x_norm y_norm]
    sigma = (1/len).*(X'*X)
    return sigma
end
