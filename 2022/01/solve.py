from sys import stdin

elf = 0
elves = []

for line in stdin:
    if line.strip() == "":
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)
elves.append(elf)

print(sorted(elves)[-1])
print(sum(sorted(elves)[-3:]))
