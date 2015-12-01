
import sys

f = open(sys.argv[1], 'r')
instructions = f.read()
been_in_the_basement = False
floor = 0
for i in range(len(instructions)):
	if instructions[i] == "(":
		floor += 1
	if instructions[i] == ")":
		floor -= 1
	if floor < 0 and not been_in_the_basement:
		print("in the basement at {}".format(i+1))
		been_in_the_basement = True
print("last floor: {}".format(floor))