""" Linear regression - Code prints out the prices of multiple cabins in one go.
"""

import math
import random
import numpy as np
import io
from io import StringIO


# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]
def predict(X, c):
    #  prints out the prices of multiple cabins in one go.
    #  write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same

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
    result_str = "\n".join(map(str, result))
    print(result_str)

predict(X, c)



