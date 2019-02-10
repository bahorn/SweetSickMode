import numpy as np
import ihash
import os
import sys

# Generate all the hashes

path = sys.argv[1]

for file in os.listdir(path):
    filename = '{}/{}'.format(path, file)
    res = ihash.generate_hash(filename)
    print(res)
