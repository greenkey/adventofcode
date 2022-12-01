from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)


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


def test_a():
    assert solve_a(puzzle.example_data) == 24000


def test_b():
    assert solve_b(puzzle.example_data) == 45000


def test_refactoring():
    if puzzle.answered_a:
        assert str(solve_a(puzzle.input_data)) == puzzle.answer_a
    if puzzle.answered_b:
        assert str(solve_b(puzzle.input_data)) == puzzle.answer_b


if __name__ == "__main__":
    if not puzzle.answered_a:
        puzzle.answer_a = solve_a(puzzle.input_data)
    print(f"A: {puzzle.answer_a}")

    if not puzzle.answered_b:
        puzzle.answer_b = solve_b(puzzle.input_data)
    print(f"B: {puzzle.answer_b}")
