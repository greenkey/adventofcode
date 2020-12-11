import sys
from itertools import product
from typing import Dict, Tuple


def run1(seats_map: Dict[Tuple[int, int], str]) -> int:
    while True:
        new_map = seats_map.copy()
        for (x, y), seat in seats_map.items():
            if seat == ".":
                continue
            occupied_around = 0
            for ax, ay in product(range(-1, 2), range(-1, 2)):
                if ax == ay == 0:
                    continue
                occupied_around += seats_map.get((x + ax, y + ay), ".") == "#"
            if seat == "L" and not occupied_around:
                new_map[x, y] = "#"
            if seat == "#" and occupied_around >= 4:
                new_map[x, y] = "L"
        if seats_map == new_map:
            break
        seats_map = new_map

    return sum(seat == "#" for seat in seats_map.values())


def go_further(n: int) -> int:
    if n > 0:
        return n + 1
    elif n < 0:
        return n - 1
    else:
        return 0


def run2(seats_map: Dict[Tuple[int, int], str]) -> int:
    base_directions = list(product(range(-1, 2), range(-1, 2)))
    base_directions.remove((0, 0))
    while True:
        new_map = seats_map.copy()
        for (x, y), seat in seats_map.items():
            if seat == ".":
                continue
            occupied_around = 0
            directions = base_directions[:]
            while directions:
                ax, ay = directions.pop()
                adj_seat = seats_map.get((x + ax, y + ay))
                if adj_seat == ".":
                    directions.append((go_further(ax), go_further(ay)))
                elif adj_seat == "#":
                    occupied_around += 1
            if seat == "L" and not occupied_around:
                new_map[x, y] = "#"
            if seat == "#" and occupied_around >= 5:
                new_map[x, y] = "L"
        if seats_map == new_map:
            break
        seats_map = new_map

    return sum(seat == "#" for seat in seats_map.values())


def solve(file_name: str):
    seats_data = open(file_name).readlines()
    seats_map = dict()
    for y, line in enumerate(seats_data):
        for x, seat in enumerate(line.strip()):
            seats_map[x, y] = seat

    print(run1(seats_map))
    print(run2(seats_map))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
