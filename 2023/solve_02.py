import run

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
        print("="*80)
        print(game)
        game_name, game = game.split(":")
        game_no = int(game_name[5:])
        print(f"Game: {game_no}")
        valid_game = True
        for subset in game.split(";"):
            if not valid_game:
                break
            parsed = _parse_set(subset)
            print(parsed)
            for colour, n in bag.items():
                if parsed.get(colour, 0) > n:
                    print("fail")
                    valid_game = False
                    break
        if valid_game:
            total += game_no
            print(f"valid, new total: {total}")
        else:
            print("invalid")
    return total


def solve_b(data):
    total = 0
    for game in data.splitlines():
        print("="*80)
        print(game)
        game_name, game = game.split(":")
        game_no = int(game_name[5:])
        print(f"Game: {game_no}")

        min_colour = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for subset in game.split(";"):
            parsed = _parse_set(subset)
            print(parsed)
            for colour, n in min_colour.items():
                if parsed.get(colour, 0) > n:
                    min_colour[colour] = parsed[colour]
        # calculate score multiplying values of min_colour
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


run.runme()
