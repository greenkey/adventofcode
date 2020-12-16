import sys


def find_scanning_error(definitions, tickets):
    allowed = set()
    for ranges in definitions.values():
        for start, end in ranges:
            allowed.update(range(start, end + 1))

    scanning_error = 0
    for ticket in tickets:
        scanning_error += sum(set(ticket).difference(allowed))

    return scanning_error


def solve(file_name: str):
    lines = open(file_name).readlines()
    your_ticket_pos = lines.index('your ticket:\n')
    my_ticket = map(int, lines[your_ticket_pos + 1].strip().split(','))
    nearby_tickets = [map(int, line.strip().split(',')) for line in lines[your_ticket_pos + 4:]]
    definitions = dict()
    for line in lines[:your_ticket_pos - 1]:
        field, ranges_str = line.split(': ')
        ranges = ranges_str.strip().split(' or ')
        definitions[field] = [
            (int(x) for x in range_.split('-'))
            for range_ in ranges
        ]

    print(find_scanning_error(definitions, nearby_tickets))


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
