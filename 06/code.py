
import re

input_mask = "(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)"

# init matrix
matrix = [[False for x in range(1000)] for x in range(1000)] 

with open("input", "r") as instructions:
    for directive in instructions:
        m = re.search(input_mask, directive)
        (action, from_x, from_y, to_x, to_y) = m.groups()
        (from_x, from_y, to_x, to_y) = map(lambda x: int(x), (from_x, from_y, to_x, to_y))
        
        print("I have to {} lights from {},{} to {},{}".format(action, from_x, from_y, to_x, to_y))
        
        for x in range(from_x,to_x+1):
            for y in range(from_y,to_y+1):
                if action == "turn on":
                    matrix[x][y] = True
                elif action == "turn off":
                    matrix[x][y] = False
                elif action == "toggle":
                    matrix[x][y] = not matrix[x][y]
        
    # count
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == True: count += 1
    print("{} lights are lit".format(count))