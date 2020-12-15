import sys
from collections import defaultdict
from typing import Dict, List


def elf_memory(starting_nums: List[int], turns: int):
    said: Dict[int, List[int]] = defaultdict(list)

    # first turns
    for turn, num in enumerate(starting_nums):
        said[num] = [turn + 1]
    last_said = starting_nums[-1]

    for turn in range(len(starting_nums) + 1, turns + 1):
        if len(said[last_said]) == 1:
            say = 0
        else:
            prev, last = said[last_said][-2:]
            say = last - prev
        said[say].append(turn)
        last_said = say

    return last_said


def test_elf_memory():
    assert elf_memory([0, 3, 6], 2020) == 436
    assert elf_memory([1, 3, 2], 2020) == 1
    assert elf_memory([2, 1, 3], 2020) == 10
    assert elf_memory([1, 2, 3], 2020) == 27
    assert elf_memory([2, 3, 1], 2020) == 78
    assert elf_memory([3, 2, 1], 2020) == 438
    assert elf_memory([3, 1, 2], 2020) == 1836


def solve(file_name: str):
    nums: List[int] = [int(x) for x in open(file_name).read().split(",")]
    print(elf_memory(nums, 2020))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
