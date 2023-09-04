import math
import random
import numpy as np
import io
from io import StringIO
def calculate_emissions(route, D, co2, portnames):
    distance = sum([D[route[i]][route[i + 1]] for i in range(len(route) - 1)])
    emissions = distance * co2
    print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)

def permutations(route, ports, D, co2, portnames):
    if not ports:
        calculate_emissions(route, D, co2, portnames)
        return

    for port in ports:
        new_route = route + [port]
        new_ports = ports.copy()
        new_ports.remove(port)
        permutations(new_route, new_ports, D, co2, portnames)

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    D = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    co2 = 0.020

    starting_port = 0  # Index of "AMS" in portnames list

    # Start the recursion with an empty route and all ports (except starting port) as unvisited
    permutations([starting_port], [p for p in range(len(portnames)) if p != starting_port], D, co2, portnames)

main()
