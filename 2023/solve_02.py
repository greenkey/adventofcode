from run import runme

year = 2023
day = 2


def solve_a(data):
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0
    for game in data.splitlines():
        game_name, game = game.split(":")
        game_no = int(game_name[5:])

        valid_game = True
        for subset in game.split(";"):
            if not valid_game:
                break
            parsed = _parse_set(subset)
            for colour, n in bag.items():
                if parsed.get(colour, 0) > n:
                    valid_game = False
                    break
        if valid_game:
            total += game_no
    return total


def solve_b(data):
    total = 0
    for game in data.splitlines():
        _, game = game.split(":")

        min_colour = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for subset in game.split(";"):
            parsed = _parse_set(subset)
            for colour, n in min_colour.items():
                if parsed.get(colour, 0) > n:
                    min_colour[colour] = parsed[colour]

        score = 1
        for n in min_colour.values():
            score *= n
        total += score

    return total


def _parse_set(s):
    result = dict()
    for cubes in s.split(","):
        n, colour = cubes.strip().split(" ")
        result[colour] = int(n)
    return result


if __name__ == "__main__":
    runme()
