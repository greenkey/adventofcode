##!/usr/bin/env python3

def getInstructions():
    with open("input") as f:
        return [int(line) for line in f.readlines()]

def cpu1(instructions):
    i = 0
    jumps = 0
    while i >= 0 and i < len(instructions):
        n = i + instructions[i]
        instructions[i] += 1
        i = n
        jumps += 1
    return jumps

def cpu2(instructions):
    i = 0
    jumps = 0
    while i >= 0 and i < len(instructions):
        n = i + instructions[i]
        if instructions[i] >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i = n
        jumps += 1
    return jumps

print(cpu1(getInstructions()))
print(cpu2(getInstructions()))