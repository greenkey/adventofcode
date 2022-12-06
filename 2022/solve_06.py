import pytest

import solve

answer_example_a = 7
answer_example_b = 19

examples = [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26),
]


def get_marker(sequence, length):
    for i in range(len(sequence) - length):
        if len(set(sequence[i : i + length])) == length:
            break
    return i + length


def solve_a(sequence):
    return get_marker(sequence, 4)


def solve_b(sequence):
    return get_marker(sequence, 14)


def test_a():
    for sequence, marker, _ in examples:
        assert (
            solve_a(sequence) == marker
        ), f"{sequence=} expecting {marker=}, got {solve_a(sequence)}"


def test_b():
    for sequence, _, marker in examples:
        assert (
            solve_b(sequence) == marker
        ), f"{sequence=} expecting {marker=}, got {solve_a(sequence)}"


if __name__ == "__main__":
    solve.main(2022, 6)
