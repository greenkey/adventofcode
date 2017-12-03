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