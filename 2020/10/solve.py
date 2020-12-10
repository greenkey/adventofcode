import re
import sys
from collections import Counter
from functools import lru_cache, reduce
from typing import List, Tuple, Dict, Optional


def solve(input_file: str):
    adapters = sorted([int(x) for x in open(input_file).readlines()])
    diffs = (
        [adapters[0]]
        + [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
        + [3]
    )
    diff_count = Counter(diffs)
    print(diff_count[1] * diff_count[3])

    s_diffs = "".join(str(x) for x in diffs)
    print(count_arrangements(s_diffs))


def count_arrangements(diffs: str) -> int:
    if len(diffs) <= 1:
        return 1
    if "3" in diffs:
        changable = diffs.split("3")
        return reduce(
            lambda x, y: x * y, [count_arrangements(part) for part in diffs.split("3")]
        )

    count = 0
    if diffs[:2] in ("21", "12"):
        count += count_arrangements(diffs[2:])
    if diffs[:2] in ("11"):
        count += count_arrangements("2" + diffs[2:])
    count += count_arrangements(diffs[1:])
    return count


def test_count_arrangements():
    assert count_arrangements("1") == 1
    assert count_arrangements("2") == 1
    assert count_arrangements("3") == 1
    assert count_arrangements("313") == 1
    assert count_arrangements("11") == 2  # 11, 2
    assert count_arrangements("21") == 2  # 21, 3
    assert count_arrangements("12") == 2  # 12, 3
    assert count_arrangements("3123") == 2  # 3123, 333
    assert count_arrangements("121") == 3  # 121, 31, 13
    assert count_arrangements("111") == 4  # 111, 21, 12, 3
    assert count_arrangements("1111") == 7  # 1111, 211, 121, 112, 22, 31, 13


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
