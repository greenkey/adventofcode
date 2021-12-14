from collections import Counter, defaultdict
from functools import lru_cache
from sys import stdin
from typing import Dict, List, Optional, Set, Tuple


class Day:
    def __init__(self, data: str):
        lines = data.splitlines()
        self.polymer = lines[0]
        self.rules: Dict[str, str] = dict(
            l.split(" -> ") for l in lines[2:]  # type: ignore
        )

    def process(self, polymer: str) -> str:
        new_polymer: List[str] = []
        for i in range(len(polymer) - 1):
            new_polymer.append(polymer[i])
            new_polymer.append(self.rules[polymer[i : i + 2]])
        new_polymer.append(polymer[-1])
        return "".join(new_polymer)

    def solve1(self) -> int:
        polymer = self.polymer
        for _ in range(10):
            polymer = self.process(polymer)
        minl = len(polymer)
        maxl = 0
        for c in Counter(polymer).values():
            minl = min(minl, c)
            maxl = max(maxl, c)
        return maxl - minl


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    print(d.solve1())
