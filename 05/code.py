
nice = 0
naughty_strings = ("ab", "cd", "pq", "xy")

with open("input", "r") as name_list:
	for name in name_list:
		naughty = False
		for ns in naughty_strings:
			if ns in name:
				naughty = True
		if not naughty:
			vowels = 0
			prev_c = ""
			twice_letter = False
			for c in name:
				if c in "aeiou": vowels += 1
				if c == prev_c:
					twice_letter = True
				prev_c = c
			if vowels >= 3 and twice_letter:
				nice += 1

print("Nice names: {}".format(nice))