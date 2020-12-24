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


def solve(file_name: str):
    tiles = Counter(path_to_xy(line.strip()) for line in open(file_name).readlines())
    blacks = [pos for pos, flips in tiles.items() if flips % 2 == 1]
    print(len(blacks))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
