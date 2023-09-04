""" Least square: program that reads cabin details and prices from a CSV file (a standard format for tabular data) and fits a linear regression model to it.
Program output is the estimated coefficients and the predicted or "fitted" prices for the same set of cabins used to estimate the parameters.
"""
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

def fit_model(input_file):
    data = np.loadtxt(input_file)
    X = np.asarray(data[:, :-1])  # Features (all columns except the last one)
    y = np.asarray(data[:, -1])   # Target (the last column)

    # read the data in and fit it. the values below are placeholder values
    c = np.linalg.inv(X.T @ X) @ X.T @ y  # coefficients of the linear regression

    print(c)
    print(X @ c)
 
# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)