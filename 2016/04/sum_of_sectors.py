
import sys, re

# Part One

def sort_longest_string_alpha(a, b):
	if len(a) == len(b):
		return ord(a[0]) - ord(b[0])
	return len(b) - len(a)

def get_checksum(room_name):
	letters = dict()
	for c in room_name:
		if c != '-':
			try:
				letters[c] += c
			except:
				letters[c] = c
	letters_sorted = sorted(letters.values())
	letters_sorted = sorted(letters_sorted, key=len, reverse=True)
	return ''.join([l[0] for l in letters_sorted[:5]])


def get_sector_id(room):
	try:
		(room_name, sector_id, checksum) = re.search('([a-z-]+)-([0-9]+)\[([^[]+)\]', room).groups()
		if get_checksum(room_name) == checksum:
			return int(sector_id)
	except:
		return 0
	return 0

with open(sys.argv[1],'r') as f:
	print(sum( [get_sector_id(l.strip()) for l in f] ))

