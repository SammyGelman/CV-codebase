#!/usr/bin/env python
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Calculate entropy from a 1D distribution.')
parser.add_argument('file', type=str,nargs='?',default="trans_dist.npz",
                           help='file to run on.')
parser.add_argument('nbins', type=int,nargs='?',default=5000,
                           help='Number of bins to generate')
parser.add_argument('-eta', type=float,nargs=1, default=1e-10,
                           help='Small constant to add to dist for log normalization')

args = parser.parse_args()
dist = np.load(args.file)

entropy = 0

for i in range(len(dist[0,:])):
    bins, edges = np.histogram(dist[:,i], bins=args.nbins)

    dx = edges[1] - edges[0]
    P = bins / np.sum(bins) / dx + args.eta
    entropy += -np.trapz(P * np.log(P), dx=dx)
    
#print("Entropy when treating transformed dist as product distribution: ",entropy)
print(entropy)

