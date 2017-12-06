##!/usr/bin/env python3

with open("input") as f:
    banks = [[int(x) for x in line.split()] for line in f.readlines()]

for bank in banks:
    combinations = dict()
    while True:
        signature = tuple(bank)
        if signature in combinations:
            print(len(combinations))
            break
        combinations[signature] = 1

        biggest = max(bank)
        i = bank.index(biggest)
        bank[i] = 0
        while biggest > 0:
            i = (i + 1) % len(bank)
            bank[i] += 1
            biggest -= 1