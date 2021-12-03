from sys import stdin


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


if __name__ == "__main__":
    data = stdin.read()
    print(Day.solve1(data))
