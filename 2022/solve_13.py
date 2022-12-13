from functools import cmp_to_key

import solve

answer_example_a = 13
answer_example_b = 140


def parse(data):
    for couple in data.split("\n\n"):
        a, b = couple.splitlines()
        yield eval(a), eval(b)


def mysort(a, b):
    if f"{a}{b}".isdigit():
        return a - b
    elif f"{a}".isdigit():
        return mysort([a], b)
    elif f"{b}".isdigit():
        return mysort(a, [b])
    # both lists
    for ai, bi in zip(a, b):
        res = mysort(ai, bi)
        if res == 0:
            continue
        else:
            return res
    return len(a) - len(b)


def solve_a(data):
    result = 0
    for i, (a, b) in enumerate(parse(data), start=1):
        if mysort(a, b) <= 0:
            result += i
    return result


def solve_b(data):
    dividers = ["[[2]]", "[[6]]"]
    data_lines = data.splitlines() + dividers
    data = [l for l in data_lines if l]
    sorted_data = sorted(map(eval, data), key=cmp_to_key(mysort))
    lines = [str(l) for l in sorted_data]
    result = 1
    for d in dividers:
        result *= lines.index(d) + 1
    return result


if __name__ == "__main__":
    solve.main(2022, 13)
