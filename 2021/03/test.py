from solve import Day

data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_case_1():
    assert Day.solve1(data) == 198


def test_oxygen():
    assert Day.extract(data.splitlines(), "oxygen") == "10111"


def test_co2():
    assert Day.extract(data.splitlines(), "co2") == "01010"


def test_case_2():
    assert Day.solve2(data) == 230
