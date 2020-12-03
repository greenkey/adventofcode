import re
from collections import Counter

file_name = 'input'

with open(file_name, 'r') as f:
    slope_map = f.readlines()

x, y = 0, 0
trees = 0
while y < len(slope_map):
    trees += slope_map[y][x] == '#'
    y += 1
    x = (x + 3) % (len(slope_map[0]) - 1)

print(trees)