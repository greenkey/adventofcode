import pytest
import solve

answer_example_a = 7
answer_example_b = 19


def solve_a(sequence):
    for i in range(len(sequence) - 4):
        if len(set(sequence[i : i + 4])) == 4:
            break
    return i + 4


def solve_b(sequence):
    for i in range(len(sequence) - 14):
        if len(set(sequence[i : i + 14])) == 14:
            break
    return i + 14


# @pytest.mark.parametrize(
#     "sequence, marker",
#     [
#         ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
#         ("nppdvjthqldpwncqszvftbrmjlhg", 6),
#         ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
#         ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
#     ],
# )
# def test_find_marker(sequence, marker):
#     assert solve_a(sequence) == marker


# @pytest.mark.parametrize(
#     "sequence, marker",
#     [
#         ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
#         ("nppdvjthqldpwncqszvftbrmjlhg", 23),
#         ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
#         ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
#     ],
# )
# def test_find_marker_2(sequence, marker):
#     assert solve_b(sequence) == marker


if __name__ == "__main__":
    solve.main(2022, None)
