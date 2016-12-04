# requires python3

import sys

keypad = [
    "123",
    "456",
    "789"
]

position = (1,1)
code = ""

with open("input", "r") as f:
    for line in f:
        for c in line.strip():
            if c == "U":
                position = (max(position[0]-1,0), position[1])
            elif c == "D":
                position = (min(position[0]+1,2), position[1])
            elif c == "R":
                position = (position[0], min(position[1]+1,2))
            elif c == "L":
                position = (position[0], max(position[1]-1,0))
        code += keypad[position[0]][position[1]]
print(code)
