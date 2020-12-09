from itertools import combinations
from typing import List, Optional


def contains_sum(data: List[int], num: int) -> bool:
    for couple in combinations(data, 2):
        if sum(couple) == num:
            return True
    return False


def find_first_invalid(data: List[int], preamble: int) -> Optional[int]:
    for i, num in enumerate(data):
        if i < preamble:
            continue
        if not contains_sum(data[i - preamble : i], num):
            return num
    return None


def solve(input_file: str):
    data = [int(x) for x in open(input_file).readlines()]
    print(find_first_invalid(data, 25))


if __name__ == "__main__":
    solve("input")
