
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

print("Nice names, first version: {}".format(nice))



nice = 0

with open("input", "r") as name_list:
	for name in name_list:
		double_couple = False
		sandwich_letter = False
		for i in range(1,len(name)):
			couple = name[i-1]+name[i]
			if couple in name[i+1:]:
				double_couple = True
		for i in range(2,len(name)):
			if name[i-2] == name[i]:
				sandwich_letter = True
		if double_couple and sandwich_letter:
			nice += 1

print("Nice names, second version: {}".format(nice))

