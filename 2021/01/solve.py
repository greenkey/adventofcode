from sys import stdin
from functools import reduce

nums = list(map(int, stdin))

prev = None
increases = 0
for num in nums:
    if prev is not None:
        increases += num > prev
    prev = num
print(increases)

prev = None
increases = 0
for i in range(len(nums)-2):
    s = sum(nums[i:i+3])
    if prev is not None:
        increases += s > prev
    prev = s
print(increases)
