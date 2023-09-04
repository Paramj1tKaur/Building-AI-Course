import math
import random
import numpy as np
import io
from io import StringIO
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def calculate_emissions(route, D, co2):
    distance = sum([D[route[i]][route[i + 1]] for i in range(len(route) - 1)])
    emissions = distance * co2
    return emissions

def permutations(route, ports):
    global smallest, bestroute

    if not ports:
        emissions = calculate_emissions(route, D, co2)
        if emissions < smallest:
            smallest = emissions
            bestroute = route.copy()
        return

    for port in ports:
        new_route = route + [port]
        new_ports = ports.copy()
        new_ports.remove(port)
        permutations(new_route, new_ports)


def main():
    starting_port = 0
    permutations([starting_port], list(range(1, len(portnames))))

    # Print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()

