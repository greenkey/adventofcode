from functools import reduce
import math
from run import runme
import re

year = 2023
day = 8

answer_example_a = "2"

example_data_b = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
answer_example_b = "6"



mask = re.compile(r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)")

def solve_a(data):
    lines = (line.strip() for line in data.splitlines())
    directions = next(lines)

    map = dict()
    for line in lines:
        if not line:
            continue
        [(node, l, r)] = mask.findall(line)
        map[node] = (l, r)

    start = "AAA"
    end = "ZZZ"
    current = start
    steps = 0
    while current != end:
        for d in directions:
            if d == "L":
                current = map[current][0]
            elif d == "R":
                current = map[current][1]
            steps += 1
            if current == end:
                break
    return steps
            


def solve_b(data):
    lines = (line.strip() for line in data.splitlines())
    directions = next(lines)

    map = dict()
    for line in lines:
        if not line:
            continue
        [(node, l, r)] = mask.findall(line)
        map[node] = (l, r)

    start = {n for n in map.keys() if n.endswith("A")}
    end = {n for n in map.keys() if n.endswith("Z")}
    step_all_paths = []

    for current in start:
        steps = 0
        while current not in end:
            for d in directions:
                if d == "L":
                    current = map[current][0]
                elif d == "R":
                    current = map[current][1]
                steps += 1
                if current == end:
                    break
        step_all_paths.append(steps)

    # Find mcm of all paths couples
    return reduce(minimum_common_multiple, step_all_paths)


def minimum_common_multiple(a, b):
    return a * b // math.gcd(a, b)


if __name__ == "__main__":
    runme()
