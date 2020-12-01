from itertools import combinations

file_name = 'input'

with open(file_name, 'r') as f:
    data = [int(line) for line in f.readlines()]

for a, b in combinations(data, 2):
    if a + b == 2020:
        print(a*b)
