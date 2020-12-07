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

print(min(abs(x) + abs(y) for (x, y), wires in grid.items() if len(wires) > 1))
