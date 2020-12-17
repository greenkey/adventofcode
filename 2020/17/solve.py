import sys
from itertools import product


def conway_n_d(space_2d, dimensions, keep_alives=(2, 3), newborn=3):
    space = {tuple([x, y] + [0] * (dimensions - 2)): cube for (x, y), cube in space_2d.items()}
    neighbors = list(product((-1, 0, 1), repeat=dimensions))
    while True:
        new_space = space.copy()
        coord_to_check = {
            tuple(c + n for c, n in zip(coord, neighbor))
            for coord, cube in space.items() if cube
            for neighbor in neighbors
        }
        for current in coord_to_check:
            cube = space.get(current, 0)
            count = sum(
                space.get(tuple(c + n for c, n in zip(current, neighbor)), 0)
                for neighbor in neighbors
            ) - cube
            if cube and count not in keep_alives:
                new_space[current] = 0
            if not cube and count == newborn:
                new_space[current] = 1
        space = {coord: cube for coord, cube in new_space.items() if cube}
        yield space


def solve(file_name: str):
    m = {'.': 0, '#': 1}
    initial_space = dict()
    for y, row in enumerate(open(file_name).readlines()):
        for x, char in enumerate(row.strip()):
            initial_space[x, y] = m[char]

    for d in (3, 4):
        for i, space in enumerate(conway_n_d(initial_space, d)):
            if i == 5:
                break
        print(f"{d}D: ", sum(space.values()))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
