import math
import re
import sys
from itertools import zip_longest
from typing import List
from itertools import product


def apply_mask(num: int, mask: str) -> int:
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


def apply_mask2(num: int, mask: str) -> str:
    value = "".join(
            [
                m if m in 'X1' else (n if n else "0")
                for m, n in zip_longest(mask[::-1], bin(num)[:1:-1])
            ][::-1]
        )
    return value


def test_apply_mask2():
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"
    assert apply_mask2(0, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"
    assert apply_mask2(1, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"
    assert apply_mask2(2, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX11"
    assert apply_mask2(3, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX11"
    assert apply_mask2(4, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"
    assert apply_mask2(5, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"
    assert apply_mask2(6, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX11"
    assert apply_mask2(7, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX11"
    assert apply_mask2(8, mask) == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX01"


def fluctuate(mask: str) -> List[str]:
    if len(mask) == 1:
        if mask == 'X':
            yield '0'
            yield '1'
        else:
            yield mask
    else:
        yield from (
            ''.join(parts)
            for parts
            in product(*(fluctuate(m) for m in mask))
        )


def test_fluctuate():
    assert set(fluctuate('0')) == {'0'}
    assert set(fluctuate('1')) == {'1'}
    assert set(fluctuate('X')) == {'1', '0'}
    assert set(fluctuate('1X')) == {'11', '10'}
    assert set(fluctuate('0X1X')) == {'0010','0011','0110','0111'}
    assert set(fluctuate('0000000000X')) == {'00000000000','00000000001'}


def solve(file_name: str):
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

    mem_mask = re.compile(r"mem\[([0-9]+)\]")
    mem = dict()
    for line in open(file_name).readlines():
        key, value = line.split(" = ")
        if key == "mask":
            mask = value.strip()
        else:
            key = int(mem_mask.findall(key)[0])
            key = apply_mask2(key, mask)
            for key in fluctuate(key):
                mem[int(key, 2)] = int(value)
    print(sum(mem.values()))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
