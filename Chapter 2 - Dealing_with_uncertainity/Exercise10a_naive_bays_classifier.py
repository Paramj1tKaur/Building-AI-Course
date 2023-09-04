""" Suppose we have two coins. One is a normal 2 euro coin that comes heads up with 50% probability, and tails up also with 50% probability. The other coin, bought from the magicians' store, has heads on both sides. 
Suppose now that we choose one of the two coins at random so that either one can be picked with equal probability. The odds that we have the normal coin is thus 1:1.
Let's say the chosen coin keeps landing heads up. 
How confident can we be that it's the magic coin?
"""

import math
import random
import numpy as np
import io
from io import StringIO
def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    for i in range(n):
        odds *= 2
    print(odds)

n = 2
flip(n)


