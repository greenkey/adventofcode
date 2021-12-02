from sys import stdin
import sys; print(sys.version)

class Day02:
    @staticmethod
    def solve1(data: str) -> int:
        horizontal = depth = 0
        for line in data.splitlines():
            # match line.split():
            #     case ["forward", n]:
            #         horizontal += int(n)
            #     case ["down", n]:
            #         depth += int(n)
            #     case ["up", n]:
            #         depth -= int(n)
            direction, n = line.split()
            if direction == "forward":
                horizontal += int(n)
            elif direction == "down":
                depth += int(n)
            elif direction == "up":
                depth -= int(n)
        return horizontal * depth

if __name__ == "__main__":
    print(Day02.solve1(stdin.read()))
