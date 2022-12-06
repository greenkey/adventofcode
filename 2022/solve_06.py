import pytest
import solve

answer_example_a = 7
answer_example_b = None


def solve_a(sequence):
    for i in range(len(sequence) - 4):
        if len(set(sequence[i : i + 4])) == 4:
            break
    return i + 4


def solve_b(data):
    return None


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


if __name__ == "__main__":
    solve.main(2022, None)
