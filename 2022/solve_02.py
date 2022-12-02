import solve

answer_example_a = 15
answer_example_b = 12


def solve_a(data):
    combinations = {
        "C X": 6 + 1,
        "A X": 3 + 1,
        "B X": 0 + 1,
        "A Y": 6 + 2,
        "B Y": 3 + 2,
        "C Y": 0 + 2,
        "C Z": 3 + 3,
        "A Z": 0 + 3,
        "B Z": 6 + 3,
    }

    score = sum(combinations[line] for line in data.splitlines())
    return score


def solve_b(data):
    """
    A=rock 1
    B=paper 2
    C=scissor 3
    X=lose
    Y=draw
    Z=win
    """
    combinations = {
        "A X": 0 + 3,
        "A Y": 3 + 1,
        "A Z": 6 + 2,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 0 + 2,
        "C Y": 3 + 3,
        "C Z": 6 + 1,
    }

    score = sum(combinations[line] for line in data.splitlines())
    return score
