from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=__CHANGE_ME__)


def solve_a(data):
    ...
    return None


def solve_b(data):
    ...
    return None


def test_a():
    assert solve_a(puzzle.example_data) == __CHANGE_ME__


def test_b():
    assert solve_b(puzzle.example_data) == __CHANGE_ME__


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
