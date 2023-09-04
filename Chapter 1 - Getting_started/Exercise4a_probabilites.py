""" Probability """

import math
import random
import numpy as np
import io
from io import StringIO
import random

def main():
    probability = random.random()
    if probability <= 0.8:
        favourite = "dog"
    else:
        favourite = "cat"
    print(favourite)

main()
  