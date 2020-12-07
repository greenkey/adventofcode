import sys
from collections import defaultdict

file_name = sys.argv[1:] or 'input'

wire_paths = [line.strip().split(',') for line in open(file_name).readlines()]

directions = {
    'U': (1, 0),
    'D': (-1, 0),
    'R': (0, 1),
    'L': (0, -1),
}

grid = defaultdict(set)

for w, wire in enumerate(wire_paths):
    pos = (0, 0)
    for step in wire:
        direction = directions[step[0]]
        for _ in range(int(step[1:])):
            pos = tuple(a + b for a, b in zip(pos, direction))
            grid[pos].add(w)

intersections = {
    (x, y) for (x, y), wires in grid.items() if len(wires) > 1
}

print(min(abs(x) + abs(y) for (x, y) in intersections))

def count_steps(path, destination):
    steps = 0
    pos = (0, 0)
    for step in path:
        direction = directions[step[0]]
        for _ in range(int(step[1:])):
            steps += 1
            pos = tuple(a + b for a, b in zip(pos, direction))
            if pos == destination:
                return steps

print(min(sum(count_steps(path, inter) for path in wire_paths) for inter in intersections))
