import solve

answer_example_a = 13
answer_example_b = None
example_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


def move(p, dir):
    x, y = p
    match dir:
        case "R":
            return x + 1, y
        case "U":
            return x, y + 1
        case "L":
            return x - 1, y
        case "D":
            return x, y - 1


def follow(from_p, to_p):
    x1, y1 = from_p
    x2, y2 = to_p
    if x1 == x2:
        if abs(y1 - y2) == 2:
            return x1, (y1 + y2) // 2
    if y1 == y2:
        if abs(x1 - x2) == 2:
            return (x1 + x2) // 2, y1

    match x1 - x2, y1 - y2:
        case (-1, 2) | (1, 2):
            return x2, y2 + 1
        case (2, -1) | (2, 1):
            return x2 + 1, y2
        case (-1, -2) | (1, -2):
            return x2, y2 - 1
        case (-2, -1) | (-2, 1):
            return x2 - 1, y2
    return from_p


def solve_a(data):
    H = T = 0, 0
    positions = {T}

    instructions = (line.split() for line in data.splitlines())

    for dir, steps in instructions:
        for _ in range(int(steps)):
            H = move(H, dir)
            T = follow(T, H)
            positions.add(T)

    return len(positions)


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 9)
