import solve

answer_example_a = 3
answer_example_b = None
example_data = """1
2
-3
3
-2
0
4
"""


def solve_a(data):
    numbers = []
    for n in map(int, data.splitlines()):
        numbers.append((n, False))
    size = len(numbers)
    to_move = size
    while to_move > 0:
        n, moved = numbers.pop(0)
        if moved:
            numbers.append((n, moved))
        else:
            if n < 0:
                move_by = -(abs(n) % (size - 1))
            else:
                move_by = n % (size - 1)
            numbers = numbers[:move_by] + [(n, True)] + numbers[move_by:]
            to_move -= 1
    zero = numbers.index((0, True))
    numbers = numbers[zero:] + numbers[:zero]
    return numbers[1000 % size][0] + numbers[2000 % size][0] + numbers[3000 % size][0]


def _test_solve_a():
    assert solve_a("\n".join(str(n) for n in [0, 1, 4]))
    "0, 4, 1 -> 4, 1, 0"
    "0, 1, 4"


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 20)
