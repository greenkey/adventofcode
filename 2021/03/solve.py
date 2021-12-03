from sys import stdin
from typing import Iterable


class Day:
    @staticmethod
    def solve1(data: str) -> int:
        lines_count = 0
        numbers = [0] * 100
        for line in data.splitlines():
            numbers = [a+b for a, b in zip(numbers, map(int, line))]
            lines_count += 1
        gamma = []
        epsilon = []
        for n in numbers:
            if n > lines_count/2:
                gamma.append("1")
                epsilon.append("0")
            else:
                gamma.append("0")
                epsilon.append("1")
        return int(''.join(gamma), 2) * int(''.join(epsilon), 2)

    @classmethod
    def solve2(cls, data: str) -> int:
        lines = data.splitlines()
        oxygen = int(cls.extract(lines, "oxygen"), 2)
        co2 = int(cls.extract(lines, "co2"), 2)
        return oxygen * co2

    @classmethod
    def extract(cls, lines: list[str], what: str) -> str:
        if len(lines) == 1:
            return lines[0]
        splitted: dict[str, list[str]] = {"0": [], "1": []}
        for line in lines:
            splitted[line[0]].append(line[1:])
        if what == "co2":
            c = str(int(len(splitted["0"]) > len(splitted["1"])))
        elif what == "oxygen":
            c = str(int(len(splitted["0"]) <= len(splitted["1"])))
        return c + cls.extract(splitted[c], what)


if __name__ == "__main__":
    data = stdin.read()
    print(Day.solve1(data))
    print(Day.solve2(data))
