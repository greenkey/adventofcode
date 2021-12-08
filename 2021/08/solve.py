from collections import Counter, defaultdict
from functools import lru_cache
from sys import stdin
from typing import Dict, List, Optional, Set, Tuple


@lru_cache()
def excl(n: int) -> int:
    return sum(range(n + 1))


class Day:
    def __init__(self, data: str):
        self.display = [[p.split() for p in l.split("|")] for l in data.splitlines()]

    def solve1(self) -> int:
        s = 0
        for p, o in self.display:
            s += len([x for x in o if len(x) in (2, 3, 4, 7)])
        return s


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    print(d.solve1())
