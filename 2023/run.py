import datetime
import importlib
from sys import argv

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

    run(m.year, m.day, m)


def run(year, day, module):
    puzzle = Puzzle(year=year, day=day)
    print(f"{puzzle.year}/{puzzle.day}: {puzzle.title}")

    # run unit tests
    run_unit_tests(module)
    print(f"Unit tests OK")

    # run parts
    for part in ["a", "b"]:
        solve_fun = getattr(module, f"solve_{part}")

        # run a with example data
        for example in puzzle.examples:
            example_data = getattr(module, f"example_data_{part}", None) or example.input_data
            answer = getattr(module, f"answer_example_{part}", None) or getattr(example, f"answer_{part}", None)
            result = str(solve_fun(example_data))
            assert (
                result == answer
            ), f"Example {part.upper()}: expecting {answer}, got {result}"
        print(f"Example {part.upper()}: OK")

        # run a with input data
        if not getattr(puzzle, f"answered_{part}"):
            setattr(puzzle, f"answer_{part}", solve_fun(puzzle.input_data))
        else:
            # regression test
            answer = str(solve_fun(puzzle.input_data))
            assert (
                getattr(puzzle, f"answer_{part}") == answer
            ), f"Real data {part.upper()} (regression): expecting {getattr(puzzle, f'answer_{part}')}, got {answer}"
        print(f"{part.upper()}: {getattr(puzzle, f'answer_{part}')}, rank={puzzle.my_stats[part]['rank']}")


if __name__ == "__main__":
    now = datetime.datetime.now()
    year = now.year
    if len(argv) < 2:
        day = now.day
    else:
        day = argv[1]

    # get day's module
    module = importlib.import_module(f"solve_{day:02d}")

    run(year, int(day), module)
