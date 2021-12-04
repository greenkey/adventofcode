from functools import reduce
from sys import stdin
from typing import List, Optional


class Day:
    @staticmethod
    def solve1(data: str) -> Optional[int]:
        lines = data.splitlines()
        numbers = lines[0].split(",")
        boards: List[List[set]] = []
        for l in lines[1:]:
            if not l:
                boards.append([])
            else:
                boards[-1].append(set(l.split()))

        for i in range(len(numbers)):
            drawn = set(numbers[: i + 1])
            for board in boards:
                for line in board:
                    if line.issubset(drawn):
                        all_board_numbers = reduce(lambda a, b: a.union(b), board)
                        undraw = all_board_numbers.difference(drawn)
                        return sum(map(int, undraw)) * int(numbers[i])
        return None


if __name__ == "__main__":
    data = stdin.read()
    print(Day.solve1(data))
