from string import ascii_letters

import solve

answer_example_a = 157
answer_example_b = 70


def solve_a(data):
    dups = []
    for line in data.splitlines():
        size = len(line) // 2
        a, b = set(line[:size]), set(line[size:])
        dups.append((a & b).pop())

    return sum([ascii_letters.find(c) + 1 for c in dups])


def solve_b(data):
    lines = [set(l) for l in data.splitlines()]
    dups = []
    for i in range(len(lines) // 3):
        a, b, c = lines[i * 3 : i * 3 + 3]
        dups.append((a & b & c).pop())

    return sum([ascii_letters.find(c) + 1 for c in dups])


if __name__ == "__main__":
    solve.main(2022, 3)
