#!/usr/bin/env python
import numpy as np

def multi_kde(data,bandwidth=0.3):
    #split distribution
    x_i = data[:,0]
    y_i = data[:,1]
    #number of samples
    n = len(x_i)
    #get standard deviation
    sigma_x = np.std(x_i)
    sigma_y = np.std(y_i)
    #create a function that takes data and outputs normal extrapolations of data
    h = 1/(sigma_x *sigma_y *bandwidth)
    def kde(x,y):
        #input a range of x and y to calculate kde on
        # X, Y = np.meshgrid(x,y)
        X = np.zeros((len(x),len(y))) 
        Y = np.zeros((len(x),len(y))) 
        for i in range(n):
    #        X = np.exp((((x[:,:,None]-x_i[None,None,:])/h)**2)/-2)
    #        Y = np.exp((((y[:,:,None]-y_i[None,None,:])/h)**2)/-2)
                X += np.exp((((x[:,None]-x_i[None,i])/h)**2)/-2)
                Y += np.exp((((y[:,None]-y_i[None,i])/h)**2)/-2) 
        est = X*np.transpose(Y)/(n*h)
    #        est = np.sum(est,axis=2)
        # est = np.sum(est,axis=1)
        return est
    return kde

