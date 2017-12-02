##!/usr/bin/env python3

with open("input") as f:
    lines = f.readlines()

total = 0
for line in lines:
    items = [int(x) for x in line.split()]
    total += max(items) - min(items)

print(total)

total = 0
for line in lines:
    items = sorted([int(x) for x in line.split()], reverse=True)
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] % items[j] == 0:
                total += items[i] / items[j]
print(int(total))