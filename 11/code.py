import sys

def next_string(string):
	c = string[-1:]
	if c == 'z':
		return next_string(string[:-1]) + 'a'
	while True:
		c = chr(ord(c)+1)
		if c not in ['i','o','l']:
			break
	return string[:-1] + c

def next_password(string):
	while True:
		string = next_string(string)

		# avoided letters
		if 'i' in string: continue
		if 'o' in string: continue
		if 'l' in string: continue

		# two pairs
		found = 0
		i = 1
		while i < len(string):
			if string[i-1] == string[i]:
				found += 1
				i += 1
			i += 1
		if found < 2:
			continue

		# increasing sequence
		found = False
		for i in range( 2, len(string) ):
			if ord(string[i-2]) + 1 == ord(string[i-1]) and ord(string[i-1]) + 1 == ord(string[i]):
				found = True
		if not found:
			continue

		return string

if __name__ == "__main__":
	print("Calculating all the passwords, press CTRL-C to stop.")
	password = sys.argv[1]
	while True:
		password = next_password(password)
		print("Next password: {}".format( password ))