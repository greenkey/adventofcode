import sys


def solve(file_name: str):
    instructions = open(file_name).readlines()

    directions = "NESW"

    x, y = 0, 0
    direction = 1
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "L":
            direction = (direction - (value // 90)) % 4
        if action == "R":
            direction = (direction + (value // 90)) % 4
        if action == "F":
            action = directions[direction]
        if action == "N":
            y += value
        if action == "S":
            y -= value
        if action == "E":
            x += value
        if action == "W":
            x -= value
    print(abs(x) + abs(y))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
