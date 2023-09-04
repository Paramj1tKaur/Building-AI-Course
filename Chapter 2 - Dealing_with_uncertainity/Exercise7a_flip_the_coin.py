""" Write a program that counts the number of occurrences of "11" in an input sequence of zeros and ones. The input of the program is just the sequence and it should return a single number, which is the number of occurrences of "11".
"""

import math
import random
import numpy as np
import io
from io import StringIO
def count11(seq):
  # Initialize the counter to 0.
  count = 0

  # Iterate over the sequence.
  for i in range(len(seq) - 1):
    # Check if the current two elements are "11".
    if seq[i] == 1 and seq[i + 1] == 1:
      # Increment the counter.
      count += 1

  # Return the number of occurrences of "11".
  return count


if __name__ == "__main__":
  # Get the input sequence from the user.
  seq = [0, 0, 1, 1, 1, 0]

  # Count the number of occurrences of "11" in the sequence.
  count = count11(seq)

  # Print the number of occurrences of "11".
  print("The number of occurrences of '11' is:", count)

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
