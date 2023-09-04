""" Bag of words: write a function that calculates the distances (or differences) between a pair of lines in the This Little Piggy rhyme.
Every row in the list data represents one line in the rhyme.
Program works with any text, not only with the rhyme This Little Piggy
"""
import math
import random
import numpy as np
import io
from io import StringIO
# this data here is the bag of words representation of This Little Piggy
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    # initialize a variable to store the sum of differences
    sum_diff = 0
    # iterate through each word's occurance in rows and calculate the absolute difference
    for i in range(len(row1)):
        diff = abs(row1[i]-row2[i])
        sum_diff += diff
    return sum_diff


def all_pairs(data):
    # this calls the distance function for all the two-row combinations in the data
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    print(dist)

all_pairs(data)