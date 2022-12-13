import solve

answer_example_a = 13
answer_example_b = None


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
    return None


if __name__ == "__main__":
    solve.main(2022, 13)
