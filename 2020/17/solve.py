import sys
from itertools import product


def solve(file_name: str):
    m = {'.': 0, '#': 1}
    initial_space = dict()
    for y, row in enumerate(open(file_name).readlines()):
        for x, char in enumerate(row.strip()):
            initial_space[x, y] = m[char]

    space = {(x, y, 0): cube for (x, y), cube in initial_space.items()}
    neighbors = list(product((-1, 0, 1), repeat=3))
    for i in range(6):
        new_space = space.copy()
        coords_to_check = {
            (nx+x, ny+y, nz+z)
            for (x, y, z), cube in space.items() if cube
            for nx, ny, nz in neighbors
        }
        for (x, y, z) in coords_to_check:
            cube = space.get((x, y, z), 0)
            count = sum(space.get((x+nx, y+ny, z+nz), 0) for nx, ny, nz in neighbors)
            if cube and count not in (3, 4):  # 2, 3 but there is the active cube at 0,0,0
                new_space[(x, y, z)] = 0
            if not cube and count == 3:
                new_space[(x, y, z)] = 1
        space = {(x, y, z): cube for (x, y, z), cube in new_space.items() if cube}
    print(sum(space.values()))

    space = {(x, y, 0, 0): cube for (x, y), cube in initial_space.items()}
    neighbors = list(product((-1, 0, 1), repeat=4))
    for i in range(6):
        new_space = space.copy()
        coords_to_check = {
            (nx+x, ny+y, nz+z, nw+w)
            for (x, y, z, w), cube in space.items() if cube
            for nx, ny, nz, nw in neighbors
        }
        for (x, y, z, w) in coords_to_check:
            cube = space.get((x, y, z, w), 0)
            count = sum(space.get((x+nx, y+ny, z+nz, w+nw), 0) for nx, ny, nz, nw in neighbors)
            if cube and count not in (3, 4):  # 2, 3 but there is the active cube at 0,0,0
                new_space[(x, y, z, w)] = 0
            if not cube and count == 3:
                new_space[(x, y, z, w)] = 1
        space = {(x, y, z, w): cube for (x, y, z, w), cube in new_space.items() if cube}
    print(sum(space.values()))

if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
