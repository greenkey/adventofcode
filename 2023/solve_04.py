from dataclasses import dataclass

from run import runme

year = 2023
day = 4

answer_example_b = str(30)


@dataclass
class Card:
    num: int
    winning_numbers: set[int]
    card_numbers: set[int]

    @staticmethod
    def parse_string(s: str) -> "Card":
        card_name, numbers = s.split(":")
        _, num = card_name.split()
        card_num = int(num)
        winning_numbers, numbers = numbers.split("|")
        winning_numbers = {int(n) for n in winning_numbers.strip().split() if n}
        card_numbers = {int(n) for n in numbers.strip().split() if n}
        return Card(card_num, winning_numbers, card_numbers)


def solve_a(data):
    total = 0
    for line in data.splitlines():
        card = Card.parse_string(line)
        winning_numbers = card.card_numbers.intersection(card.winning_numbers)
        if winning_numbers:
            total += 2 ** (len(winning_numbers) - 1)
    return total


def solve_b(data):
    initial_cards = [Card.parse_string(line) for line in data.splitlines()]
    won_cards = {card.num: 1 for card in initial_cards}
    for card in initial_cards:
        winning_numbers = card.card_numbers.intersection(card.winning_numbers)
        for i in range(len(winning_numbers)):
            won_cards[card.num + 1 + i] += won_cards[card.num]

    return sum(won_cards.values())


if __name__ == "__main__":
    runme()
