from functools import reduce
from itertools import combinations

file_name = 'input'

with open(file_name, 'r') as f:
    data = [int(line) for line in f.readlines()]

for a, b in combinations(data, 2):
    if a + b == 2020:
        print(a * b)

for nums in combinations(data, 3):
    if sum(nums) == 2020:
        print(reduce(lambda a, b: a * b, nums))
