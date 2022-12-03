from string import ascii_letters

import solve

answer_example_a = 157
answer_example_b = None


def solve_a(data):
    dups = []
    for line in data.splitlines():
        size = len(line) // 2
        a, b = set(line[:size]), set(line[size:])
        dups.append((a & b).pop())

    return sum([ascii_letters.find(c)+1 for c in dups])


def solve_b(data):
    return None
