#!/usr/bin/env python
import numpy as np
import tensorflow as tf
import pickle
import random

def num_flip(num_flips,num_samples,percent_flip,L):
    data = np.ones((num_samples,L,L))*-1
    for i in range(int(percent_flip * len(data[:,0,0]))):
        for flip in range(num_flips):
            idx_1 = random.randint(0,L-1)
            idx_2 = random.randint(0,L-1)
            data[i,idx_1,idx_2] = 1
    path = 'flips.npz'
    np.savez(path ,*data[:len(data)])
    





    def sample_prep(sample):
        sample = np.array(sample)
        sample = np.where(sample==-1,0,sample)
        sample = sample[..., np.newaxis]
        sample_dict = {'image': sample, 'label': ()}
        return sample_dict

    def get_samples(filename):
        samples = np.load(filename)
        for sname in samples.files:
            yield sample_prep(samples[sname])

    shape = (int(L),int(L),1)
    ds_samples = tf.data.Dataset.from_generator(
        get_samples,
        # args=['/gcohenlab/data/samuelgelman/data/ising_data/ising_samples_l'+str(L)+'/T'+str(T)+'/samples_rank'+str(int(batch))+'.npz'],
        args=[str(path)],
        output_types={'image': tf.int64, 'label': tf.float64},
        output_shapes={'image': shape, 'label': None}
        )
    ds_samples = tf.data.Dataset.prefetch(ds_samples,1)
    return shape, ds_samples
