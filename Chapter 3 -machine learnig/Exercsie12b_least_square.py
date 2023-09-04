""" Least square - program to calculate the squared error for multiple sets of coefficient values and print out the index of the set that yields the smallest squared error.
"""
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   
def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
        # Calculate the predicted price
        prediction = xi @ c
        # prediction = np.dot(xi, c)
        # Subtract the predicted price from the actual price yi
        diff = yi - prediction
        # Square the difference and add it to sse
        sse += diff ** 2
    return sse

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for i, coeff in enumerate(c):
        # Calculate the sum of squared errors for the current coefficient set
        error = squared_error(X, y, coeff)
        # Check if the current error is smaller than the smallest error found so far
        if error < smallest_error:
            smallest_error = error
            best_index = i
    print("the best set is set %d" % best_index)

find_best(X, y, c)
