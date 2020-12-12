import sys
from typing import List


def rules_1(instructions: List[str]) -> (int, int):
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
    return x, y


def rules_2(instructions: List[str]) -> (int, int):
    sx, sy = 0, 0   # absolute position
    wx, wy = 10, 1  # relative position
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "L":
            magic = [wx, wy, -wx, -wy] * 2
            i = 4 - ((value // 90) % 4)
            wx, wy = magic[i:i + 2]
        if action == "R":
            magic = [wx, wy, -wx, -wy] * 2
            i = (value // 90) % 4
            wx, wy = magic[i:i + 2]
        if action == "F":
            for i in range(value):
                sx += wx
                sy += wy
        if action == "N":
            wy += value
        if action == "S":
            wy -= value
        if action == "E":
            wx += value
        if action == "W":
            wx -= value

    return sx, sy


def solve(file_name: str):
    instructions = open(file_name).readlines()

    x, y = rules_1(instructions)
    print(abs(x) + abs(y))

    x, y = rules_2(instructions)
    print(abs(x) + abs(y))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
