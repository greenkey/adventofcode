from collections import Counter
from typing import Iterable

from run import runme

year = 2023
day = 7


def solve_a(data: str):
    hand_list = OrderedList()
    for line in data.splitlines():
        hand_list.insert(parse_line(line))
    return sum(hand.bid * i for i, hand in enumerate(hand_list.iterate(), start=1))


def solve_b(data):
    return None


def parse_line(card_line: str) -> "Hand":
    cards, bid_str = card_line.split()
    return Hand(cards, int(bid_str))


card_value_order = "23456789TJQKA"


class Hand:
    def __init__(self, cards: str, bid: int) -> None:
        self.cards: str = cards
        self.bid: int = bid
        self.type_score = self._type_score()

    def _type_score(self) -> int:
        c = Counter(self.cards)
        if sorted(c.values()) == [5]:
            return 7
        if sorted(c.values()) == [1, 4]:
            return 6
        if sorted(c.values()) == [2, 3]:
            return 5
        if sorted(c.values()) == [1, 1, 3]:
            return 4
        if sorted(c.values()) == [1, 2, 2]:
            return 3
        if sorted(c.values()) == [1, 1, 1, 2]:
            return 2
        if sorted(c.values()) == [1, 1, 1, 1, 1]:
            return 1
        raise ValueError("Invalid hand")

    def __lt__(self, other: "Hand"):
        if self.type_score != other.type_score:
            return self.type_score < other.type_score
        for card, other_card in zip(self.cards, other.cards):
            if card != other_card:
                return card_value_order.index(card) < card_value_order.index(other_card)
        return False


def test_hand_type_score():
    hand = Hand("AAAAA", 1)
    assert hand.type_score == 7

    hand = Hand("AA8AA", 1)
    assert hand.type_score == 6

    hand = Hand("23332", 1)
    assert hand.type_score == 5

    hand = Hand("TTT98", 1)
    assert hand.type_score == 4

    hand = Hand("23432", 1)
    assert hand.type_score == 3

    hand = Hand("A23A4", 1)
    assert hand.type_score == 2

    hand = Hand("23456", 1)
    assert hand.type_score == 1


def test_hand_lt():
    assert Hand("33332", 1) > Hand("2AAAA", 1)
    assert Hand("77888", 1) > Hand("77788", 1)
    assert Hand("AAAAA", 1) > Hand("KKKKK", 1)
    assert Hand("AAAAA", 1) > Hand("AA8AA", 1)
    assert Hand("AA8AA", 1) > Hand("23332", 1)
    assert Hand("23332", 1) > Hand("TTT98", 1)
    assert Hand("TTT98", 1) > Hand("23432", 1)
    assert Hand("23432", 1) > Hand("A23A4", 1)
    assert Hand("A23A4", 1) > Hand("23456", 1)


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class OrderedList:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value, node: Node | None = None):
        if node is None:
            node = self.root
        if node is None:
            self.root = Node(value)
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)

    def iterate(self) -> Iterable:
        yield from self._iterate(self.root)

    def _iterate(self, node: Node | None = None) -> Iterable:
        if node is not None:
            yield from self._iterate(node.left)
            yield node.value
            yield from self._iterate(node.right)


def test_ordered_insert():
    l = OrderedList()
    assert list(l.iterate()) == []
    l.insert(1)
    assert list(l.iterate()) == [1]
    l.insert(2)
    assert list(l.iterate()) == [1, 2]
    l.insert(0)
    assert list(l.iterate()) == [0, 1, 2]
    l.insert(3)
    assert list(l.iterate()) == [0, 1, 2, 3]
    l.insert(1)
    assert list(l.iterate()) == [0, 1, 1, 2, 3]


if __name__ == "__main__":
    runme()
