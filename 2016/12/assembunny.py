import sys

with open(sys.argv[1],'r') as f:
	code = [l.split() for l in f.read().split('\n')]

register = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0
}
for i in range(len(sys.argv[2:])):
	register[sorted(register.keys())[i]] = int(sys.argv[i+2])

i = 0
while i < len(code):
	line = code[i]
	if line:
		if line[0] == 'cpy':
			try:
				register[line[2]] = int(line[1])
			except ValueError as e:
				register[line[2]] = register[line[1]]
		elif line[0] == 'inc':
			register[line[1]] += 1
		elif line[0] == 'dec':
			register[line[1]] -= 1
		
		if line[0] == 'jnz':
			try:
				v = register[line[1]]
			except KeyError as e:
				v = int(line[1])
			if v > 0:
				i += int(line[2])
				continue
	i += 1

print(register)
