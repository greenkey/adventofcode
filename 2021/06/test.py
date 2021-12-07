from solve import Day

data = """3,4,3,1,2"""


def test_case_1():
    assert Day(data).solve1(80) == 5934
