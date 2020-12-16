"""
Very awful code, I wanted to refactor it but I'm done for today
"""
import sys
from collections import defaultdict
from functools import reduce


def solve(file_name: str):
    lines = open(file_name).readlines()

    your_ticket_pos = lines.index('your ticket:\n')

    my_ticket = [int(x) for x in lines[your_ticket_pos + 1].strip().split(',')]

    nearby_tickets = [[int(x) for x in line.strip().split(',')] for line in lines[your_ticket_pos + 4:]]

    allowed_num_by_field = dict()
    for line in lines[:your_ticket_pos - 1]:
        field, ranges_str = line.split(': ')
        ranges = ranges_str.strip().split(' or ')
        allowed = set()
        for start, end in [
            (int(x) for x in range_.split('-'))
            for range_ in ranges
        ]:
            allowed.update(range(start, end + 1))
        allowed_num_by_field[field] = allowed

    allowed = reduce(lambda a, b:  a.union(b), allowed_num_by_field.values())
    values_per_field = [set() for _ in range(len(my_ticket))]
    scanning_error = 0
    for ticket in nearby_tickets[:]:
        not_allowed = set(ticket).difference(allowed)
        if not_allowed:
            scanning_error += sum(not_allowed)
            nearby_tickets.remove(ticket)
            continue
        for i, n in enumerate(ticket):
            values_per_field[i].add(n)

    print(scanning_error)

    possible_i = defaultdict(set)
    for field, allowed in allowed_num_by_field.items():
        for i, real in enumerate(values_per_field):
            if real.issubset(allowed):
                possible_i[field].add(i)
    found = dict()
    while len(found) < len(my_ticket):
        for field, possible in possible_i.items():
            if len(possible) == 1:
                found[field] = list(possible)[0]
        for field, possible in possible_i.items():
            possible.difference_update(found.values())
    print(found)

    departure = 1
    for field, i in found.items():
        if field.startswith('departure'):
            departure *= my_ticket[i]
    print(departure)


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
