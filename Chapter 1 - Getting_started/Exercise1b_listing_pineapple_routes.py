import math
import random
import numpy as np
import io
from io import StringIO
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    for port in ports:
            new_route = route + [port]
            new_ports = ports.copy()
            new_ports.remove(port)
            permutations(new_route, new_ports)
    if len(ports) == 0:
        print(' '.join([portnames[i] for i in route]))
        return
permutations([0], list(range(1, len(portnames))))