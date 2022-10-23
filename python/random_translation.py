import numpy as np
import tensorflow as tf
import random

def random_translation(old):
    l = len(old)
    print("This is the val for l: ",str(l))
    i_r = random.randint(0,l)
    j_r = random.randint(0,l)
    print("This is the random i index: ", str(i_r))
    print("This is the random j index: ", str(j_r))

    i_shift = l-i_r
    j_shift = l-j_r

    old_arr = np.array(old)

    new_arr = np.zeros(np.shape(old_arr))

    for i in range(l+1):
        print(i)
        for j in range(l+1):
            if i+i_shift > l:
                new_i_idx = (i+i_shift-1)%l
            else:    
                new_i_idx = i+i_shift
            
            if j+j_shift > l:
                new_j_idx = (j+j_shift-1)%l
            else:    
                new_j_idx = j+j_shift
                
            new_arr[new_i_idx,new_j_idx]=old_arr[i,j]

    print(tf.arr(old_arr))
    print(new_arr)
