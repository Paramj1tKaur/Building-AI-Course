""" Nearest neighbor:  calculate the Euclidean distance between two vectors.
"""
import numpy as np

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)