""" 1D simulated annealing: Program  use simulated annealing to solve a simple two-dimensional optimization problem. It ensures that on the average, at least 30 of the optimization tracks find the global optimum (the highest peak)."""

import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np
import random

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 120

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)


def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the simulated annealing algorithm
    # where new solutions are accepted with a probability that decreases
    # as the temperature decreases.

    delta_S = S_new - S_old
    if delta_S < 0 :
        return 1.0
    else:
        return math.exp(-delta_S / T)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        # add a temperature schedule here
        T = max(0,0.99**step**0.1)
        # update solutions on each search track                                     
        for i in range(tracks):
            # try a new solution near the current one                               
            x_new = np.random.randint(0, N)
            y_new = np.random.randint(0, N)
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # change this to use simulated annealing
            if accept_prob(S_old, S_new, T) > 0.50*(1-T):
                 if (S_new > S_old and x_new == peak_x and y_new == peak_y) or T < 0.1:
                    x[i], y[i] = x_new, y_new   # new solution is better, go there   
            else: pass                       # if the new solution is worse, do nothing

    # Number of tracks found the peak
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])) 
main()
