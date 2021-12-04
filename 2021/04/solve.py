from functools import reduce
from sys import stdin
from typing import List, Optional, Set


class Board:
    def __init__(self, data: str):
        self.lines: List[Set[str]] = []
        items = [l.split() for l in data.splitlines()]
        trans = [[items[j][i] for j in range(len(items))] for i in range(len(items[0]))]
        self.lines = [set(l) for l in items] + [set(c) for c in trans]

    def all_numbers(self) -> Set[str]:
        s: Set[str] = set()
        for line in self.lines:
            s = s.union(line)
        return s

    def check(self, drawn: List[str]) -> int:
        for line in self.lines:
            if line.issubset(drawn):
                undraw = self.all_numbers().difference(drawn)
                return sum(map(int, undraw)) * int(drawn[-1])
        return 0


class Day:
    def __init__(self, data: str):
        numbers, *boards = data.split("\n\n")
        self.numbers = numbers.split(",")
        self.boards: List[Board] = [Board(t) for t in boards]

    def get_winners(self):
        for i in range(len(self.numbers)):
            for board in self.boards:
                points = board.check(self.numbers[: i + 1])
                if points:
                    self.boards.remove(board)
                    yield points

    def solve1(self) -> int:
        return next(self.get_winners())

    def solve2(self) -> int:
        all_winners = list(self.get_winners())
        return all_winners[-1]


if __name__ == "__main__":
    data = stdin.read()
    d = Day(data)
    print(d.solve1())
    print(d.solve2())
