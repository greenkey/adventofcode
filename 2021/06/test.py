from solve import Day

data = """3,4,3,1,2"""


def test_case_1():
    assert Day(data).solve1(80) == 5934


def test_case_2():
    assert Day(data).solve2(18) == 26
    assert Day(data).solve2(256) == 26984457539
