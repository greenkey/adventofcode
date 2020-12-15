import sys
from typing import List
import math

def solve(file_name: str = "input", *params: List[str]):
    image_data = open(file_name).read().strip()
    image_size = 25 * 6
    
    best_layer = {'0': image_size, '1': 0, '2': 0}
    count = best_layer.copy()
    for i, c in enumerate(image_data):
        if i % image_size == 0:
            if count['0'] < best_layer['0']:
                least_0 = count['0']
                best_layer = count.copy()
            count = {'0': 0, '1': 0, '2': 0}
        count[c] += 1
    if count['0'] < least_0:
        least_0 = count['0']
        best_layer = count.copy()
    
    print(best_layer['1'] * best_layer['2'])



if __name__ == "__main__":
    solve(*sys.argv[1:])
