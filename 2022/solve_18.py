import solve

answer_example_a = 64
answer_example_b = None

side_deltas = [
    (0, 0, +1),
    (0, 0, -1),
    (0, +1, 0),
    (0, -1, 0),
    (+1, 0, 0),
    (-1, 0, 0),
]


def solve_a(data):
    shown_sides = 0
    occupied_places = set()

    for line in data.splitlines():
        q, r, s = coord = tuple([int(x) for x in line.split(",")])
        sides = 6
        for dq, dr, ds in side_deltas:
            if (q + dq, r + dr, s + ds) in occupied_places:
                sides -= 2
        occupied_places.add(coord)
        shown_sides += sides

    return shown_sides


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 18)
