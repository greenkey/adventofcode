from collections import Counter, defaultdict
from sys import stdin
from typing import Dict, List, Optional, Set, Tuple


class Day:
    def __init__(self, data: str):
        self.fishes = [int(f) for f in data.split(",")]

    def day_passed(self):
        for i in range(len(self.fishes)):
            fish = self.fishes[i]
            fish -= 1
            if fish < 0:
                fish = 6
                self.fishes.append(8)
            self.fishes[i] = fish

    def solve1(self, n: int) -> int:
        for _ in range(n):
            self.day_passed()
        return len(self.fishes)

    def solve2(self, n: int) -> int:
        fishes = Counter(self.fishes)
        for _ in range(n):
            n: Dict[int, int] = {
                8: fishes[0],
                7: fishes[8],
                6: fishes[0] + fishes[7],
                5: fishes[6],
                4: fishes[5],
                3: fishes[4],
                2: fishes[3],
                1: fishes[2],
                0: fishes[1],
            }
            fishes = n
        return sum(fishes.values())


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    # print(d.solve1(80))
    print(d.solve2(256))
