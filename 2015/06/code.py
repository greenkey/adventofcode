
import re

input_mask = "(.*) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)"

size = 1000

# init matrix
matrix1 = [[False for x in range(size)] for x in range(size)] 
matrix2 = [[0 for x in range(size)] for x in range(size)] 

with open("input", "r") as instructions:
    for directive in instructions:
        m = re.search(input_mask, directive)
        (action, from_x, from_y, to_x, to_y) = m.groups()
        (from_x, from_y, to_x, to_y) = map(lambda x: int(x), (from_x, from_y, to_x, to_y))
        
        #print("I have to {} lights from {},{} to {},{}".format(action, from_x, from_y, to_x, to_y))
        
        for x in range(from_x,to_x+1):
            for y in range(from_y,to_y+1):
                if action == "turn on":
                    matrix1[x][y] = True
                    matrix2[x][y] += 1
                elif action == "turn off":
                    matrix1[x][y] = False
                    matrix2[x][y] -= 1
                    if matrix2[x][y] < 0: matrix2[x][y] = 0
                elif action == "toggle":
                    matrix1[x][y] = not matrix1[x][y]
                    matrix2[x][y] += 2
        
    # count
    count1 = 0
    count2 = 0
    for x in range(size):
        for y in range(size):
            if matrix1[x][y] == True: count1 += 1
            count2 += matrix2[x][y]
    print("{} lights are lit (version 1)".format(count1))
    print("{} total brightness (version 2)".format(count2))
    