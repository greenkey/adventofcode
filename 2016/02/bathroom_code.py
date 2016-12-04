# requires python3

import sys

keypad1 = [
    "123",
    "456",
    "789"
]
keypad2 = [
    "  1  ",
    " 234 ",
    "56789",
    " ABC ",
    "  D  "
]

keypad = keypad2
position = (2,0)
code = ""

with open("input", "r") as f:
    for line in f:
        for c in line.strip():
            if c == "U":
                np = (max(position[0]-1,0), position[1])
            elif c == "D":
                np = (min(position[0]+1,len(keypad)-1), position[1])
            elif c == "R":
                np = (position[0], min(position[1]+1,len(keypad[position[0]])-1))
            elif c == "L":
                np = (position[0], max(position[1]-1,0))
            if keypad[np[0]][np[1]] != " ":
                position = np
        code += keypad[position[0]][position[1]]
print(code)
