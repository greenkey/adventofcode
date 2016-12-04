# requires python3

import sys

directions = 'NESW'

instructions = sys.argv[1].split(', ')

current_position = (0, 0)
current_direction = 0 #N
positions_visited = [(0,0)]

for i in instructions:
    if i[0] == 'R':
        current_direction += 1
    elif i[0] == 'L':
        current_direction -= 1
    current_direction = current_direction % 4

    steps = int(i[1:])

    for n in range(steps):
        if current_direction == 0: #North
            current_position = (current_position[0], current_position[1]+1)
        elif current_direction == 1: #East
            current_position = (current_position[0]+1, current_position[1])
        elif current_direction == 2: #South
            current_position = (current_position[0], current_position[1]-1)
        elif current_direction == 3: #West
            current_position = (current_position[0]-1, current_position[1])

        if current_position in positions_visited:
            print("Already been here: {} - distance: {}".format(current_position, abs(sum(current_position)) ))

        positions_visited.append(current_position)

print("Final position: {} - distance: {}".format(current_position, abs(sum(current_position)) ))
