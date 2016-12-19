import sys
from math import ceil

elf_no = int(sys.argv[1])

print("Part One")
elfs = list(range(1,elf_no+1))
while len(elfs)>1:
	if len(elfs)%2 == 0:
		elfs = elfs[::2]
	elif len(elfs)>1:
		elfs = elfs[::2][1:]
print(elfs[0])


def f1(elf_no):
	elfs = list(range(1,elf_no+1))
	while len(elfs)>1:
		elf = elfs.pop(0)
		elfs.remove(elfs[int(ceil(len(elfs)/2))-1])
		elfs.append(elf)
	print(elfs[0])

def f2(elf_no):
	elfs = list(range(1,elf_no+1))
	mid = int(ceil(len(elfs)/2))-1
	elfs = elfs[mid:] + elfs[:mid]
	if len(elfs)%2 == 1:
		elfs = elfs[1:]
	while len(elfs)>1:
		elfs = elfs[3:] + [elfs[0]]
	print(elfs[0])

def f3(elf_no):
	elfs = list(range(1,elf_no+1))
	mid = int(ceil(len(elfs)/2))-1
	elfs = elfs[mid:] + elfs[:mid]
	if len(elfs)%2 == 1:
		elfs = elfs[1:]
	while len(elfs)>1:
		if len(elfs)%3 == 0:
			elfs = elfs[::3]
		elfs = elfs[3:] + [elfs[0]]
	print(elfs[0])

print("Part Two")
#f1(elf_no)
#f2(elf_no)
f3(elf_no)