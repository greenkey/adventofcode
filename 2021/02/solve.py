import sys


class Day02:
    @staticmethod
    def solve1(data: str) -> int:
        horizontal = depth = 0
        for line in data.splitlines():
            match line.split():
                case["forward", n]:
                    horizontal += int(n)
                case["down", n]:
                    depth += int(n)
                case["up", n]:
                    depth -= int(n)
            # direction, n = line.split()
            # if direction == "forward":
            #     horizontal += int(n)
            # elif direction == "down":
            #     depth += int(n)
            # elif direction == "up":
            #     depth -= int(n)
        return horizontal * depth

    @staticmethod
    def solve2(data: str) -> int:
        horizontal = depth = aim = 0
        for line in data.splitlines():
            direction, n = line.split()
            if direction == "forward":
                horizontal += int(n)
                depth += int(n) * aim
            elif direction == "down":
                aim += int(n)
            elif direction == "up":
                aim -= int(n)
        return horizontal * depth


if __name__ == "__main__":
    data = stdin.read()
    print(Day02.solve1(data))
    print(Day02.solve2(data))
