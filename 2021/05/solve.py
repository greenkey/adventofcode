from collections import defaultdict
from sys import stdin
from typing import Dict, List, Optional, Set, Tuple


class Day:
    def __init__(self, data: str):
        self.lines: List[tuple] = []
        for line in data.splitlines():
            point1, point2 = line.split(" -> ")
            self.lines.append(
                (
                    tuple(int(x) for x in point1.split(",")),
                    tuple(int(x) for x in point2.split(",")),
                )
            )

    def create_map(self):
        m = defaultdict(int)
        for (x1, y1), (x2, y2) in self.lines:
            if x1 == x2:
                y1, y2 = min(y1, y2), max(y1, y2)
                for y in range(y1, y2 + 1):
                    m[(x1, y)] += 1
            elif y1 == y2:
                x1, x2 = min(x1, x2), max(x1, x2)
                for x in range(x1, x2 + 1):
                    m[(x, y1)] += 1
        return m

    def print_map(self, m: Dict[Tuple[int, int], int]):
        x1 = y1 = 0
        for x, y in m.keys():
            x1 = max(x, x1)
            y1 = max(y, y1)
        print("  " + "".join(str(i)[-1] for i in range(x1 + 1)))
        for y in range(y1 + 1):
            print(str(y)[-1], end=" ")
            for x in range(x1 + 1):
                v = m[(x, y)]
                print(v if v else ".", end="")
            print()
        print()

    def solve1(self) -> int:
        m = self.create_map()
        # self.print_map(m)
        return sum(1 for x in m.values() if x > 1)


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    print(d.solve1())
