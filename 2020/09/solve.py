from itertools import combinations
from typing import List, Optional


def contains_sum(data: List[int], num: int) -> bool:
    for couple in combinations(data, 2):
        if sum(couple) == num:
            return True
    return False


def find_first_invalid(data: List[int], preamble: int) -> int:
    for i, num in enumerate(data):
        if i < preamble:
            continue
        if not contains_sum(data[i - preamble : i], num):
            return i
    return -1


def find_encryption_weakness(
    data: List[int], first_invalid_position: int
) -> Optional[int]:
    for i in range(first_invalid_position):
        for j in range(i, first_invalid_position):
            if sum(data[i:j]) == data[first_invalid_position]:
                return min(data[i:j]) + max(data[i:j])
    return None


def solve(input_file: str):
    data = [int(x) for x in open(input_file).readlines()]

    position = find_first_invalid(data, 25)
    print(data[position])

    encryption_weakness = find_encryption_weakness(data, position)
    print(encryption_weakness)


if __name__ == "__main__":
    solve("input")
