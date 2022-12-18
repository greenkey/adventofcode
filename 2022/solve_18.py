from time import sleep

import solve

answer_example_a = 64
answer_example_b = 58

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
    untouched_sides = 0
    occupied_places = set()
    min_q = None
    max_q = None
    min_r = None
    max_r = None
    min_s = None
    max_s = None

    for line in data.splitlines():
        q, r, s = coord = tuple([int(x) for x in line.split(",")])
        min_q = min(q, min_q) if min_q else q
        max_q = max(q, max_q) if max_q else q
        min_r = min(r, min_r) if min_r else r
        max_r = max(r, max_r) if max_r else r
        min_s = min(s, min_s) if min_s else s
        max_s = max(s, max_s) if max_s else s
        sides = 6
        for dq, dr, ds in side_deltas:
            if (q + dq, r + dr, s + ds) in occupied_places:
                sides -= 2
        occupied_places.add(coord)
        untouched_sides += sides

    all_places = set()
    for q in range(min_q, max_q + 1):
        for r in range(min_r, max_r + 1):
            for s in range(min_s, max_s + 1):
                all_places.add((q, r, s))

    unused_places = all_places - occupied_places
    border_places = set(
        (q, r, s)
        for q, r, s in unused_places
        if q in (min_q, max_q) or r in (min_r, max_r) or s in (min_s, max_s)
    )
    bp_queue = list(border_places)
    while True:
        try:
            q, r, s = bp_queue.pop()
        except IndexError:
            break
        for dq, dr, ds in side_deltas:
            this = (q + dq, r + dr, s + ds)
            if this in border_places:
                continue
            if this in unused_places:
                border_places.add(this)
                bp_queue.append(this)

    internal_places = unused_places - border_places
    exposed_sides = untouched_sides
    for q, r, s in internal_places:
        sides = 0
        for dq, dr, ds in side_deltas:
            if (q + dq, r + dr, s + ds) in occupied_places:
                sides -= 1
        occupied_places.add(coord)
        exposed_sides += sides

    return exposed_sides


if __name__ == "__main__":
    solve.main(2022, 18)
