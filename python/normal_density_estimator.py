#!/usr/bin/env python
import numpy as np
import matplotlib as plt

#x is a linspace of interest
#x_i is our set of IDD
#h sets out bandwidth
#to do: vectorize

def density_est(x, x_i, h): 
    
    vals = len(x) 
    samples = len(x_i) 

    x_dense = np.zeros((vals,samples))
    
    for i in range(vals):
        x_dense[:,i] = x
   
    print("This is x_dense: ", x_dense)

    y_dense = np.zeros((vals,samples))    
    
    y_dense = np.exp(-(((x-x_i[i])/h)**2)) 
    
  #  y_dense = sum(y_dense,axis=1)/(samples*h)
    
    plt.plot(x,y_dense) 
    plt.show()
    return y_dense
