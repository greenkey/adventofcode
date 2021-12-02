from solve import Day02

data = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def test_input():
    assert Day02.solve1(data) == 150