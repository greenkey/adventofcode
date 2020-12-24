import sys
from collections import Counter, defaultdict


def path_to_xy(path):
    counter = defaultdict(int)
    prev = None
    for c in path:
        if c in 'ns':
            prev = c
            continue
        elif c in 'we':
            if prev:
                counter[prev+c] += 1
                prev = None
            else:
                counter[c] += 1
    counter['ne'] -= counter['sw']; del counter['sw']
    counter['se'] -= counter['nw']; del counter['nw']
    counter['e'] -= counter['w']; del counter['w']
    ne, e, se = counter['ne'], counter['e'], counter['se']
    x = e * 2 + se + ne
    y = ne - se
    return x, y


def apply_flip_rules(tiles, life=(2,), death=(0, 3, 4, 5, 6)):
    adj_pos = ((2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1))
    new_tiles = set(tiles)
    board = tiles | {(x + ax, y + ay) for ax, ay in adj_pos for x, y in tiles}
    for x, y in board:
        adjacents = {(x + ax, y + ay) for ax, ay in adj_pos if (x + ax, y + ay) in tiles}
        if (x, y) in tiles and len(adjacents) in death:
            new_tiles.remove((x, y))
        elif (x, y) not in tiles and len(adjacents) in life:
            new_tiles.add((x, y))
    return new_tiles


def test_flip_rules():
    assert apply_flip_rules({(1, 1), (2, 0)}) == {(1, 1), (2, 0), (0, 0)}


def solve(file_name: str):
    tiles = Counter(path_to_xy(line.strip()) for line in open(file_name).readlines())
    blacks = {pos for pos, flips in tiles.items() if flips % 2 == 1}
    print(len(blacks))

    for i in range(100):
        blacks = apply_flip_rules(blacks)

    print(len(blacks))

if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
