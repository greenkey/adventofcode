import re
from collections import defaultdict


def create_map(squares):
    fabric = defaultdict(list)
    for name, start_x, start_y, width, height in squares:
        for x in range(start_x, start_x+width):
            for y in range(start_y, start_y+height):
                fabric[(x,y)].append(name)
    return fabric

def contended_inches(fabric_map):
    return len([inch for inch in fabric_map.values() if len(inch) > 1])

def get_non_overlapping_clain(fabric_map):
    all_names = set()
    overlapping_names = set()
    for inch in fabric_map.values():
        all_names.update(inch)
        if len(inch) > 1:
            overlapping_names.update(inch)

    return all_names - overlapping_names

if __name__ == '__main__':
    # #1 @ 1,3: 4x4
    mask = re.compile(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$')
    with open('input') as f:
        squares = [
            [int(x) for x in mask.findall(line)[0]]
            for line in f.readlines()
        ]

    fabric_map = create_map(squares)
    print(contended_inches(fabric_map))
    print(get_non_overlapping_clain(fabric_map))
