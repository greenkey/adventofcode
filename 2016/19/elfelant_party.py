import sys

elf_no = int(sys.argv[1])

elfs = list(range(1,elf_no+1))
while len(elfs)>1:
	if len(elfs)%2 == 0:
		elfs = elfs[::2]
	elif len(elfs)>1:
		elfs = elfs[::2][1:]
print(elfs[0])
