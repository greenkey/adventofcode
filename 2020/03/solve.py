import re
from collections import Counter
from functools import reduce

file_name = 'input'

with open(file_name, 'r') as f:
    slope_map = f.readlines()

slopes = {
    (1, 1): 0,
    (3, 1): 0,
    (5, 1): 0,
    (7, 1): 0,
    (1, 2): 0,
}

for right, down in slopes.keys():
    x, y = 0, 0
    while y < len(slope_map):
        slopes[right, down] += slope_map[y][x] == '#'
        y += down
        x = (x + right) % (len(slope_map[0]) - 1)

print(slopes[3, 1])
print(reduce(lambda a, b: a * b, slopes.values()))