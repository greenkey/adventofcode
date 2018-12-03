import re
from collections import defaultdict


def contended_inches(squares):
    fabric = defaultdict(list)
    max_x, max_y = 0, 0
    for name, start_x, start_y, width, height in squares:
        for x in range(start_x, start_x+width):
            for y in range(start_y, start_y+height):
                fabric[(x,y)].append(name)
                max_x = x if x > max_x else max_x
                max_y = y if y > max_y else max_y

    return len([inch for inch in fabric.values() if len(inch) > 1])

if __name__ == '__main__':
    # #1 @ 1,3: 4x4
    mask = re.compile(r'^#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)$')
    with open('input') as f:
        squares = [
            [int(x) for x in mask.findall(line)[0]]
            for line in f.readlines()
        ]

    print(contended_inches(squares))
