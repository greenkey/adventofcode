##!/usr/bin/env python3

import sys

n = int(sys.argv[1])

circles = 0
biggest = 1
side = 0

while biggest < n:
    circles += 1
    side = side + 2
    for i in range(1, 5):
        biggest += side
        if biggest > n:
            break

nearest_center = int(biggest-side/2)
distance = n-nearest_center+circles
print(distance)


from collections import defaultdict

def get_adjacent_sum(map, x, y):
    #print(x, y)
    s = 0
    for X in range(x-1, x+2):
        if X in map:
            for Y in range(y-1, y+2):
                if Y in map[X]:
                    s += map[X][Y]
    map[x][y] = s
    #print_map(map)
    return s

def print_map(map):
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for x, col in map.items():
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        for y, val in map[x].items():
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            
    print ("=====")
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if y in map[x]:
                val = map[x][y]
            else:
                val = ""
            print("{:<10}".format(val), end="")
        print("\n")
    print ("=====")

map = defaultdict(dict)
x, y = 0, 0
map[x][y] = 1
side = 0
while True:
    x += 1
    s = get_adjacent_sum(map, x, y)
    if s > n:
        print(s)
        exit(0)
    side += 2
    for j in range(side-1): #going up
        y += 1
        s = get_adjacent_sum(map, x, y)
        if s > n:
            print(s)
            exit(0)
    for j in range(side): #going left
        x -= 1
        s = get_adjacent_sum(map, x, y)
        if s > n:
            print(s)
            exit(0)
    for j in range(side): #going down
        y -= 1
        s = get_adjacent_sum(map, x, y)
        if s > n:
            print(s)
            exit(0)
    for j in range(side): #going right
        x += 1
        s = get_adjacent_sum(map, x, y)
        if s > n:
            print(s)
            exit(0)
