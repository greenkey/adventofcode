import sys
from collections import Counter, defaultdict


STEP_TO_XY = {
    'ne': (1, 1),
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
}


def path_to_xy(path):
    x, y = 0, 0
    prev = None
    for c in path:
        if c in 'ns':
            prev = c
            continue
        elif c in 'we':
            if prev:
                dx, dy = STEP_TO_XY[prev+c]
                prev = None
            else:
                dx, dy = STEP_TO_XY[c]
            x += dx
            y += dy
    return x, y


ADJ_POS = ((2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1))


def apply_flip_rules(tiles, life=(2,), death=(0, 3, 4, 5, 6)):
    new_tiles = set(tiles)
    board = tiles | {(x + ax, y + ay) for ax, ay in ADJ_POS for x, y in tiles}
    for x, y in board:
        adjacent = len([(x + ax, y + ay) for ax, ay in ADJ_POS if (x + ax, y + ay) in tiles])
        if (x, y) in tiles and adjacent in death:
            new_tiles.remove((x, y))
        elif (x, y) not in tiles and adjacent in life:
            new_tiles.add((x, y))
    return new_tiles


def solve(file_name: str):
    tiles = Counter(path_to_xy(line.strip()) for line in open(file_name).readlines())
    blacks = {pos for pos, flips in tiles.items() if flips % 2 == 1}
    print(len(blacks))

    for i in range(100):
        blacks = apply_flip_rules(blacks)
    print(len(blacks))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
