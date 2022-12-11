import re

import solve

answer_example_a = 10605
answer_example_b = None

monkey_mask = re.compile(
    r"""Monkey ([0-9]+):
  Starting items: ([0-9]+(, ([0-9]+))*)
  Operation: new = (.+)
  Test: divisible by ([0-9]+)
    If true: throw to monkey ([0-9]+)
    If false: throw to monkey ([0-9]+)""",
    re.MULTILINE,
)


class Monkey:
    def __init__(self, data):
        info = monkey_mask.findall(data)[0]
        self.monkey_id = int(info[0])
        self.items = [int(x) for x in info[1].split(", ")]
        self.operation = info[-4]
        self.divisible_by = int(info[-3])
        self.if_divisible_to = int(info[-2])
        self.if_not_divisible_to = int(info[-1])
        self.activity = 0

    def turn(self):
        while self.items and (old := self.items.pop(0)):
            value = eval(self.operation)
            value = value // 3
            if value % self.divisible_by == 0:
                yield value, self.if_divisible_to
            else:
                yield value, self.if_not_divisible_to
            self.activity += 1

    def add_item(self, item):
        self.items.append(item)


def solve_a(data):
    monkeys = []
    for monkey_data in data.split("\n\n"):
        monkeys.append(Monkey(monkey_data))

    for round in range(20):
        for monkey in monkeys:
            for item, to_monkey in monkey.turn():
                monkeys[to_monkey].add_item(item)

    business = [m.activity for m in monkeys]
    m1, m2 = sorted(business)[-2:]

    return m1 * m2


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 11)
