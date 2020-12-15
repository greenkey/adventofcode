import sys
from typing import List
import math

def solve(file_name: str = "input", *params: List[str]):
    image_data = open(file_name).read().strip()
    image_sizes = 25, 6
    image_size = image_sizes[0] * image_sizes[1]
    
    best_layer = {'0': image_size, '1': 0, '2': 0}
    count = best_layer.copy()
    visible_layer = ['2'] * image_size
    for i, c in enumerate(image_data):
        if i % image_size == 0:
            if count['0'] < best_layer['0']:
                least_0 = count['0']
                best_layer = count.copy()
            count = {'0': 0, '1': 0, '2': 0}
        count[c] += 1
        if visible_layer[i % image_size] not in '01':
            visible_layer[i % image_size] = c
    if count['0'] < least_0:
        least_0 = count['0']
        best_layer = count.copy()
    
    print(best_layer['1'] * best_layer['2'])

    for i in range(image_sizes[1]):
        a, b = i*image_sizes[0], (i+1)*image_sizes[0]
        print(''.join(visible_layer[a:b]).replace('0', ' ').replace('1', '#'))



if __name__ == "__main__":
    solve(*sys.argv[1:])
