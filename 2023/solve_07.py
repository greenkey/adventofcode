from collections import Counter
from typing import Callable, Iterable

from run import runme

year = 2023
day = 7


def solve_a(data: str):
    hand_list = OrderedList()
    for line in data.splitlines():
        cards, bid_str = line.split()
        hand_list.insert(Hand(cards, int(bid_str)))
    return sum(hand.bid * i for i, hand in enumerate(hand_list.iterate(), start=1))


def solve_b(data):
    hand_list = OrderedList()
    for line in data.splitlines():
        cards, bid_str = line.split()
        hand_list.insert(Hand(cards, int(bid_str), wildcard="J"))
    return sum(hand.bid * i for i, hand in enumerate(hand_list.iterate(), start=1))


class Hand:
    scoring = {
        (5,): 7,
        (1, 4): 6,
        (2, 3): 5,
        (1, 1, 3): 4,
        (1, 2, 2): 3,
        (1, 1, 1, 2): 2,
        (1, 1, 1, 1, 1): 1,
    }

    def __init__(
        self,
        cards: str,
        bid: int,
        wildcard: str = "",
    ) -> None:
        self.cards: str = cards
        self.bid: int = bid
        self.card_value_order = "23456789TJQKA"
        if wildcard:
            self.card_value_order = wildcard + self.card_value_order.replace(
                wildcard, ""
            )
        self.type_score = self._type_score(cards, wildcard=wildcard)

    def _type_score(self, cards, wildcard: str = "") -> int:
        c = Counter(cards)

        score = self.scoring[tuple(sorted(c.values()))]

        if wildcard and wildcard in c:
            for most_common, _ in c.most_common():
                if most_common != wildcard:
                    return self._type_score(cards.replace(wildcard, most_common))

        return score

    def __lt__(self, other: "Hand"):
        if self.type_score != other.type_score:
            return self.type_score < other.type_score
        for card, other_card in zip(self.cards, other.cards):
            if card != other_card:
                return self.card_value_order.index(card) < self.card_value_order.index(other_card)
        return False


def test_hand_type_score():
    # Five of a kind (5)
    hands = [
        Hand("AAAAA", 1),
        Hand("AAJAA", 1, wildcard="J"),
        Hand("AJJJJ", 1, wildcard="J"),
    ]
    assert all(hand.type_score == 7 for hand in hands)

    # Four of a kind (4+1)
    hands = [
        Hand("AA8AA", 1),
        Hand("2333J", 1, wildcard="J"),
        Hand("T55J5", 1, wildcard="J"),
        Hand("KTJJT", 1, wildcard="J"),
        Hand("QQQJA", 1, wildcard="J"),
    ]
    assert all(hand.type_score == 6 for hand in hands)

    # Full house (3+2)
    hands = [
        Hand("23332", 1),
        Hand("T55TJ", 1, wildcard="J"),
    ]
    assert all(hand.type_score == 5 for hand in hands)

    # Three of a kind (3+1+1)
    hands = [
        Hand("TTT98", 1),
        Hand("TTJ98", 1, wildcard="J"),
    ]
    assert all(hand.type_score == 4 for hand in hands)

    # Two pair (2+2+1)
    hands = [
        Hand("23432", 1),
    ]
    assert all(hand.type_score == 3 for hand in hands)

    # One pair (2+1+1+1)
    hands = [
        Hand("A23A4", 1),
        Hand("A23J4", 1, wildcard="J"),
    ]
    assert all(hand.type_score == 2 for hand in hands)

    # High card (1+1+1+1+1)
    hands = [Hand("23456", 1)]
    assert all(hand.type_score == 1 for hand in hands)


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

    assert Hand("JKKK2", 1, wildcard="J") < Hand("QQQQ2", 1, wildcard="J")
    assert Hand("J22AA", 1, wildcard="J") < Hand("22AAA", 1, wildcard="J")


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
