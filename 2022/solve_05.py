import re
from collections import defaultdict
from string import ascii_letters

import solve

answer_example_a = "CMZ"
answer_example_b = "MCD"


cols_to_take = [1, 5, 9, 13, 17, 21, 25, 29, 33]
mask = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")


def parse_crates(data) -> dict:
    crates = defaultdict(list)
    for line in data.splitlines():
        for crate, pos in enumerate(cols_to_take, start=1):
            if pos > len(line):
                break
            item = line[pos].strip()
            if item.isnumeric():
                return crates
            if item:
                crates[str(crate)].insert(0, item)


def get_top_item(crates: dict) -> str:
    return "".join([crates[str(i)].pop() for i in range(1, 10) if str(i) in crates])


def solve_a(data):
    first, second = data.split("\n\n")
    crates = parse_crates(first)

    for line in second.splitlines():
        [(n, from_crate, to_crate)] = mask.findall(line)
        for _ in range(int(n)):
            crates[to_crate].append(crates[from_crate].pop())

    return get_top_item(crates)


def solve_b(data):
    first, second = data.split("\n\n")
    crates = parse_crates(first)

    for line in second.splitlines():
        [(n, from_crate, to_crate)] = mask.findall(line)
        crates[to_crate].extend(crates[from_crate][-int(n) :])
        crates[from_crate] = crates[from_crate][: -int(n)]

    return get_top_item(crates)


if __name__ == "__main__":
    solve.main(2022, 5)
