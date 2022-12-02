import solve

answer_example_a = 24000
answer_example_b = 45000


def get_elves(data):
    elf = 0

    for line in data.splitlines():
        if line.strip() == "":
            yield elf
            elf = 0
        else:
            elf += int(line)
    yield elf


def solve_a(data):
    elves = list(get_elves(data))
    return sorted(elves)[-1]


def solve_b(data):
    elves = list(get_elves(data))
    return sum(sorted(elves)[-3:])
