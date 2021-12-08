from solve import Day

data = """16,1,2,0,4,2,7,1,2,14"""


def test_case_1():
    assert Day(data).solve1() == 37
