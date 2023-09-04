""" Bag of words:  program that calculates the distances (or differences) between every pair of lines in the This Little Piggy rhyme and finds the most similar pair. It uses the Manhattan distance (also called Taxicab distance) as the distance metric.
"""
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def manhattan_distance(row1, row2):
    return np.sum(np.abs(np.array(row1) - np.array(row2)))

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)

    for i in range(N):
        for j in range(N):
            if i != j:
                dist[i][j] = manhattan_distance(data[i], data[j])
            else:
                dist[i][j] = np.inf              
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
