""" Least square - program to implement the calculation of the squared error 
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
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values


def squared_error(X, y, c):
    sse = 0.0
    for xi, yi in zip(X, y):
         # Calculate the predicted price
        prediction = xi @ c
        # Subtract the predicted price from the actual price yi
        diff = yi - prediction
        # Square the difference and add it to sse
        sse += diff ** 2
        pass
    print(sse)

squared_error(X, y, c)
