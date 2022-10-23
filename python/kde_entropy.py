import numpy as np

def kde_entropy(x,y,z,n_bins_x,n_bins_y):
    #Find max and min for x and y
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)

    x_range = x_max - x_min
    y_range = y_max - y_min

    #Turn x and y into the bins they will go into
    bin_x = (np.floor((x - x_min)/x_range*(n_bins_x - 1)))
    bin_y = (np.floor((y - y_min)/y_range*(n_bins_y - 1)))
    
    bin_x = bin_x.astype(int)
    bin_y = bin_y.astype(int)

    #set matrix for entropy
    M = np.zeros((n_bins_x,n_bins_y))

    #place data in respective bins
    for i in range(len(x)):
        for j in range(len(y)):
            M[bin_x[i],bin_y[j]] += z[i,j]
    print(M)

    #calculate the probability of landing at any index in matrix M 
    dx = x_range/n_bins_x
    dy = y_range/n_bins_y

    M = M / len(x) / (dx*dy)
    M = M + 10**(-20)

    #calculate the entropy of the system
    entropy = -sum(sum(np.log(M)*M))*(dx*dy)
    return(entropy)
