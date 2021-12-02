from solve import Day02

data = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_case_1():
    assert Day02.solve1(data) == 150


def test_case_2():
    assert Day02.solve2(data) == 900
