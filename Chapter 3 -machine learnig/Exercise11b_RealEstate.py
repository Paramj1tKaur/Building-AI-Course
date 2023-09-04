""" Linear regression - Program that process multiple cabins that may be described by any number of details (like five below), at the same time assuming each of the lists contained in the list x and the coefficients c contain the same number of elements.
"""

import math
import random
import numpy as np
import io
from io import StringIO

# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    #  process multiple cabins that may be described by any number of details (like five below), at the same time. You can assume that each of the lists contained in the list x and the coefficients c contain the same number of elements.

    # Check if the dimensions are compatible for multiplication
    num_rows_X = len(X)
    num_cols_X = len(X[0])
    num_elements_c = len(c)

    if num_cols_X != num_elements_c:
        print("Matrix and vector dimensions are not compatible for multiplication.")
    else:
        # Initialize the result vector with zeros
        result = [0] * num_rows_X

    # Perform the matrix-vector multiplication
    for i in range(num_rows_X):
        for j in range(num_cols_X):
            result[i] += X[i][j] * c[j]

    # Print the result as a newline-separated string
    price = "\n".join(map(str, result))
    print(price)

predict(X, c)


