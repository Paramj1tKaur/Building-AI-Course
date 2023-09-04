""" Probability with sentence"""

import math
import random
import numpy as np
import io
from io import StringIO
import random

def main():
    probability = random.random()

    if probability < 0.8:
        favourite = "dogs"
    elif probability < 0.9:
        favourite = "cats"
    else:
        favourite = "bats"

    print("I love " + favourite)

main()