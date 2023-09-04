""" Least square: program that reads data about one set of cabins (training data), estimates linear regression coefficients based on it, then reads data about another set of cabins (test data), and predicts the prices in it.
"""
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    train = StringIO(train_string)
    test = StringIO(test_string)

    data_train = np.genfromtxt(train, skip_header=1)
    data_test = np.genfromtxt(test, skip_header=1)

    # read in the training data and separate it to x_train and y_train
    x_train = np.asarray(data_train[:, :-1])  # Features (all columns except the last one)
    y_train = np.asarray(data_train[:, -1])     
    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train, rcond =-1)[0]

    # read in the test data and separate x_test from it
    x_test = np.asarray(data_test[:, :-1]) 

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)

main()





