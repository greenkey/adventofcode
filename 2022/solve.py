from aocd.models import Puzzle


def main(year, day):
    puzzle = Puzzle(year=year, day=day)
    print(f"{puzzle.year}/{puzzle.day}: {puzzle.title}")

    m = __import__(f"solve_{day:02}")
    if hasattr(m, "example_data"):
        example_data = m.example_data
    else:
        example_data = p.example_data

    # test module
    for attr_name in m.__dict__:
        if not attr_name.startswith("test_"):
            continue
        if not callable(fun := getattr(m, attr_name)):
            continue
        fun()

    # test a
    assert (
        m.solve_a(example_data) == m.answer_example_a
    ), f"expecting {m.answer_example_a}, got {m.solve_a(example_data)}"

    # solve a
    if not puzzle.answered_a:
        puzzle.answer_a = m.solve_a(puzzle.input_data)
    else:
        # regression test
        answer = str(m.solve_a(puzzle.input_data))
        assert puzzle.answer_a == answer, (puzzle.answer_a, answer)
    print(f"A: {puzzle.answer_a}, rank={puzzle.my_stats['a']['rank']}")

    # test b
    assert (
        m.solve_b(example_data) == m.answer_example_b
    ), f"expecting {m.answer_example_b}, got {m.solve_b(example_data)}"

    # solve b
    if not puzzle.answered_b:
        puzzle.answer_b = m.solve_b(puzzle.input_data)
    else:
        # regression test
        answer = str(m.solve_b(puzzle.input_data))
        assert puzzle.answer_b == answer, (puzzle.answer_b, answer)
    print(f"A: {puzzle.answer_b}, rank={puzzle.my_stats['b']['rank']}")


if __name__ == "__main__":
    from sys import argv

    year = "2022"
    if len(argv) < 2:
        day = input("day:")
    else:
        day = argv[1]

    main(year, int(day))
