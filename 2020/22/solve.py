import sys
from copy import deepcopy


def combat(players):
    while all(players):
        cards = [deck.pop(0) for deck in players]
        winner = cards.index(max(cards))
        players[winner] += sorted(cards, reverse=True)

    for deck in players:
        if deck:
            return sum((i + 1) * n for i, n in enumerate(deck[::-1]))


def recursive_combat(players, calculate_score=False):
    seen = set()
    while all(players):
        game = tuple(tuple(deck) for deck in players)
        if game in seen:
            return 0
        seen.add(game)
        cards = [deck.pop(0) for deck in players]
        if all(len(deck) >= card for deck, card in zip(players, cards)):
            winner = recursive_combat([deck[:card] for card, deck in zip(cards, players)])
        else:
            winner = cards.index(max(cards))
        players[winner] += [cards.pop(winner)] + list(cards)

    if calculate_score:
        for deck in players:
            if deck:
                return sum((i + 1) * n for i, n in enumerate(deck[::-1]))
    return winner


def solve(file_name: str):
    players = [[int(line) for line in player.split('\n')[1:]] for player in open(file_name).read().split('\n\n')]

    print(combat(deepcopy(players)))

    print(recursive_combat(deepcopy(players), calculate_score=True))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
