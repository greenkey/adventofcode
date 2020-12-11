import sys
from itertools import product


def solve(file_name: str):
    seats_data = open(file_name).readlines()
    seats_map = dict()
    for y, line in enumerate(seats_data):
        for x, seat in enumerate(line.strip()):
            seats_map[x, y] = seat

    while True:
        new_map = seats_map.copy()
        for (x, y), seat in seats_map.items():
            if seat == '.':
                continue
            occupied_around = 0
            for ax, ay in product(range(-1, 2), range(-1, 2)):
                if ax == ay == 0:
                    continue
                occupied_around += seats_map.get((x+ax, y+ay), '.') == '#'
            if seat == 'L' and not occupied_around:
                new_map[x, y] = '#'
            if seat == '#' and occupied_around >= 4:
                new_map[x, y] = 'L'
        if seats_map == new_map:
            break
        seats_map = new_map

    print(sum(seat == '#' for seat in seats_map.values()))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else 'input')
