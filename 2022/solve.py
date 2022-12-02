from aocd.models import Puzzle

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

    # test a
    assert m.solve_a(puzzle.example_data) == m.answer_example_a

    # solve a
    if not puzzle.answered_a:
        puzzle.answer_a = m.solve_a(puzzle.input_data)
    else:
        # regression test
        answer = str(m.solve_a(puzzle.input_data))
        assert puzzle.answer_a == answer, (puzzle.answer_a, answer)
    print(f"A: {puzzle.answer_a}, rank={puzzle.my_stats['a']['rank']}")

    # test b
    assert m.solve_b(puzzle.example_data) == m.answer_example_b

    # solve b
    if not puzzle.answered_b:
        puzzle.answer_b = m.solve_b(puzzle.input_data)
    else:
        # regression test
        answer = str(m.solve_b(puzzle.input_data))
        assert puzzle.answer_b == answer, (puzzle.answer_b, answer)
    print(f"A: {puzzle.answer_b}, rank={puzzle.my_stats['b']['rank']}")
