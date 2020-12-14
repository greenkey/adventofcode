import math
import re
import sys
from itertools import zip_longest


def apply_mask(num: int, mask: str):
    value = int(
        "".join(
            [
                m if m in "01" else (n if n else "0")
                for m, n in zip_longest(mask[::-1], bin(num)[:1:-1])
            ][::-1]
        ),
        2,
    )
    return value


def test_apply_mask():
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"
    assert apply_mask(0, mask) == 1
    assert apply_mask(1, mask) == 1
    assert apply_mask(2, mask) == 1
    assert apply_mask(3, mask) == 1
    assert apply_mask(4, mask) == 5
    assert apply_mask(5, mask) == 5
    assert apply_mask(6, mask) == 5
    assert apply_mask(7, mask) == 5
    assert apply_mask(8, mask) == 9


def solve(file_name: str):
    mem_mask = re.compile(r"mem\[([0-9]+)\]")
    mask = "X" * 36
    mem = dict()
    for line in open(file_name).readlines():
        key, value = line.split(" = ")
        if key == "mask":
            mask = value.strip()
        else:
            value = apply_mask(int(value), mask)
            mem[key] = value
    print(sum(mem.values()))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
