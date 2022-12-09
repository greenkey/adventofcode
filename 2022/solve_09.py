import solve

answer_example_a = 13
answer_example_b = 1
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

    # first analyze "horse position"
    if (abs(x1 - x2) + abs(y1 - y2)) == 3:
        match x1 - x2, y1 - y2:
            case (-1, 2) | (1, 2):
                return x2, y2 + 1
            case (2, -1) | (2, 1):
                return x2 + 1, y2
            case (-1, -2) | (1, -2):
                return x2, y2 - 1
            case (-2, -1) | (-2, 1):
                return x2 - 1, y2

    # in all the other cases we only need to reduce the coordinate diff from 2 to 1
    new_x, new_y = from_p
    if abs(y1 - y2) == 2:
        new_y = (y1 + y2) // 2
    if abs(x1 - x2) == 2:
        new_x = (x1 + x2) // 2
    return new_x, new_y


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
    # 0 = H, -1 = T
    rope = [(0, 0)] * 10
    positions = {rope[-1]}

    instructions = (line.split() for line in data.splitlines())

    for dir, steps in instructions:
        for _ in range(int(steps)):
            rope[0] = move(rope[0], dir)
            for i in range(9):
                rope[i + 1] = follow(rope[i + 1], rope[i])
            positions.add(rope[-1])

    return len(positions)


def test_b():
    data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
    result = solve_b(data)
    assert result == 36, result


if __name__ == "__main__":
    solve.main(2022, 9)
