from collections import Counter, defaultdict
from functools import lru_cache
from sys import stdin
from typing import Dict, List, Optional, Set, Tuple


@lru_cache()
def excl(n: int) -> int:
    return sum(range(n + 1))


class Day:
    def __init__(self, data: str):
        self.crabs = [int(x) for x in data.split(",")]

    def solve1(self) -> int:
        fuel = sum(self.crabs)
        for a in range(1, max(self.crabs) + 1):
            fuel = min(fuel, sum(abs(c - a) for c in self.crabs))
        return fuel

    def solve2(self) -> int:
        fuel = sum(excl(c) for c in self.crabs)
        for a in range(1, max(self.crabs) + 1):
            fuel = min(fuel, sum(excl(abs(c - a)) for c in self.crabs))
        return fuel


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    print(d.solve1())
    print(d.solve2())
