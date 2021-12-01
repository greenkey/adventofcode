from sys import stdin
from functools import reduce

prev = None
increases = 0
for num in map(int, stdin):
    if prev is not None:
        increases += num > prev
    prev = num
print(increases)
