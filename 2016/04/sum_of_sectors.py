
import sys, re

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

def get_room_info(room_string):
	try:
		return re.search('([a-z-]+)-([0-9]+)\[([^[]+)\]', room_string).groups()
	except Exception as e:
		raise e

def get_sector_id(room):
	try:
		(room_name, sector_id, checksum) = get_room_info(room)
		if get_checksum(room_name) == checksum:
			return int(sector_id)
	except Exception as e:
		raise e
	return 0

def shift_cipher(room_name, sector_id):
	k1 = ord('a')
	k2 = ord('z')-k1+1
	return ''.join( [' ' if l == '-' else chr( ((ord(l)-k1+sector_id)%k2)+k1 ) for l in room_name] )

# Part One
with open(sys.argv[1],'r') as f:
	print(sum( [get_sector_id(l.strip()) for l in f] ))

# Part Two
with open(sys.argv[1],'r') as f:
	for room in f:
		(room_name, sector_id, checksum) = get_room_info(room)
		real_room_name = shift_cipher(room_name, int(sector_id))
		if "north" in real_room_name:
			print("The room '{}' is in sector {}".format(real_room_name, sector_id))

