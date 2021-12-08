from collections import Counter, defaultdict
from sys import stdin
from typing import Dict, List, Optional, Set, Tuple


class Day:
    def __init__(self, data: str):
        self.crabs = [int(x) for x in data.split(",")]

    def solve1(self) -> int:
        fuel = sum(self.crabs)
        for a in range(1, max(self.crabs) + 1):
            fuel = min(fuel, sum(abs(c - a) for c in self.crabs))
        return fuel


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    print(d.solve1())
