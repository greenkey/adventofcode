from sys import stdin

elf = 0
biggest_elf = 0
elves = []

for line in stdin:
    if line.strip() == "":
        biggest_elf = max(biggest_elf, elf)
        elves.append(elf)
        elf = 0
    else:
        elf += int(line)
biggest_elf = max(biggest_elf, elf)
elves.append(elf)

print(biggest_elf)
print(sum(sorted(elves)[-3:]))
