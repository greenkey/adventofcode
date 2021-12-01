from functools import reduce
from sys import stdin
from typing import Iterable

nums = list(map(int, stdin))


def get_increases(nums: Iterable[int]) -> int:
    prev = None
    increases = 0
    for num in nums:
        if prev is not None:
            increases += num > prev
        prev = num
    return increases


print(get_increases(nums))
print(get_increases([sum(nums[i:i+3]) for i in range(len(nums)-2)]))
