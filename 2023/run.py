import datetime
import importlib
import os
from sys import argv
from unittest.mock import patch

from aocd.models import Puzzle


def run_unit_tests(m):
    # get test functions
    test_functions = []
    for attr_name in m.__dict__:
        if not attr_name.startswith("test_"):
            continue
        if not callable(fun := getattr(m, attr_name)):
            continue
        test_functions.append(fun)
    # run tests
    for fun in test_functions:
        fun()


def runme():
    # get caller module using call stack
    import inspect
    caller = inspect.stack()[1]
    m = inspect.getmodule(caller[0])

    if getattr(m, "DEBUG", False):
        print("DEBUG MODE ON")
        run(m.year, m.day, m)
    else:
        with patch("builtins.print"):
            run(m.year, m.day, m)


def run(year, day, module):
    puzzle = Puzzle(year=year, day=day)
    print(f"{puzzle.year}/{puzzle.day}: {puzzle.title}")

    # run unit tests
    run_unit_tests(module)
    print(f"Unit tests OK")

    # run a with example data
    example_data_a = getattr(module, "example_data_a", puzzle.example_data)
    result = module.solve_a(example_data_a)
    assert (
        result == module.answer_example_a
    ), f"Example A: expecting {module.answer_example_a}, got {result}"
    print(f"Example A: OK")

    # run a with input data
    if not puzzle.answered_a:
        puzzle.answer_a = module.solve_a(puzzle.input_data)
    else:
        # regression test
        answer = str(module.solve_a(puzzle.input_data))
        assert (
            puzzle.answer_a == answer
        ), f"Real data A (regression): expecting {puzzle.answer_a}, got {answer}"
    print(f"A: {puzzle.answer_a}, rank={puzzle.my_stats['a']['rank']}")

    # run b with example data
    example_data_b = getattr(module, "example_data_b", puzzle.example_data)
    result = module.solve_b(example_data_b)
    assert (
        result == module.answer_example_b
    ), f"Example B: expecting {module.answer_example_b}, got {result}"
    print(f"Example B: OK")

    # run b with input data
    if not puzzle.answered_b:
        puzzle.answer_b = module.solve_b(puzzle.input_data)
    else:
        # regression test
        answer = str(module.solve_b(puzzle.input_data))
        assert (
            puzzle.answer_b == answer
        ), f"Real data B (regression): expecting {puzzle.answer_b}, got {answer}"
    print(f"B: {puzzle.answer_b}, rank={puzzle.my_stats['b']['rank']}")


if __name__ == "__main__":
    # discover all days
    days = []
    for filename in os.listdir("."):
        if filename.startswith("solve_") and filename.endswith(".py"):
            days.append(int(filename[6:8]))
            importlib.import_module(f"solve_{filename[6:8]}")

    now = datetime.datetime.now()
    year = now.year
    if len(argv) < 2:
        day = now.day
    else:
        day = argv[1]

    run(year, int(day))
