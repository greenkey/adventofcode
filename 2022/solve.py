from aocd.models import Puzzle


class Solution:
    def __init__(self, data):
        self.data = data

    @property
    def answer_example_a(self):
        raise NotImplementedError

    @property
    def answer_example_b(self):
        raise NotImplementedError

    def solve_a(self):
        raise NotImplementedError

    def solve_b(self):
        raise NotImplementedError


if __name__ == "__main__":
    from sys import argv

    year = "2022"
    if len(argv) < 2:
        day = f"0{input('day:')}"[-2:]
    else:
        day = f"0{argv[1]}"[-2:]
    puzzle = Puzzle(year=2022, day=int(day))
    print(f"{puzzle.year}/{puzzle.day}: {puzzle.title}")

    m = __import__(f"solve_{day}")

    # test module
    for attr_name in m.__dict__:
        if not attr_name.startswith("test_"):
            continue
        if not callable(fun := getattr(m, attr_name)):
            continue
        fun()

    e = m.Solution(puzzle.example_data)
    s = m.Solution(puzzle.input_data)

    # test a
    assert e.solve_a() == e.answer_example_a

    # solve a
    if not puzzle.answered_a:
        puzzle.answer_a = s.solve_a()
    else:
        # regression test
        assert puzzle.answer_a == str(s.solve_a()), (puzzle.answer_a, str(s.solve_a()))
    print(f"A: {puzzle.answer_a}, rank={puzzle.my_stats['a']['rank']}")

    # test b
    assert e.solve_b() == e.answer_example_b

    # solve b
    if not puzzle.answered_b:
        puzzle.answer_b = s.solve_b()
    else:
        # regression test
        assert puzzle.answer_b == str(s.solve_b()), (puzzle.answer_b, str(s.solve_b()))
    print(f"B: {puzzle.answer_b}, rank={puzzle.my_stats['b']['rank']}")
