from string import ascii_letters

import solve

answer_example_a = 2
answer_example_b = 4


def solve_a(data):
    count = 0
    for line in data.splitlines():
        (a_start, a_end), (b_start, b_end) = [
            [int(x) for x in range.split("-")] for range in line.split(",")
        ]
        if a_start <= b_start and a_end >= b_end:
            count += 1
        elif b_start <= a_start and b_end >= a_end:
            count += 1
    return count


def solve_b(data):
    count = 0
    for line in data.splitlines():
        (a_start, a_end), (b_start, b_end) = [
            [int(x) for x in range.split("-")] for range in line.split(",")
        ]
        if b_start <= a_start <= b_end:
            count += 1
        elif b_start <= a_end <= b_end:
            count += 1
        elif a_start <= b_end <= a_end:
            count += 1
        elif a_start <= b_start <= a_end:
            count += 1
    return count


def test_overlap():
    data = "\n".join(["5-10,5-10"])
    assert solve_a(data) == 1


if __name__ == "__main__":
    solve.main(2022, 4)
