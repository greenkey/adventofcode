
def next_tile_row(row):
	row = '.' + row + '.'
	ret = ''
	for i in range(1,len(row)-1):
		buf = row[i-1:i+2]
		if buf in ['^^.','.^^','^..','..^']:
			ret += '^'
		else:
			ret += '.'
	return ret


if __name__ == '__main__':

	import sys

	try:
		first_row = open(sys.argv[1]).read().strip()
	except:
		first_row = sys.argv[1]

	tiles = [first_row]
	for i in range(int(sys.argv[2])-1):
		tiles.append(next_tile_row(tiles[-1]))

	#print('\n'.join(tiles))
	print(sum([sum([1 if c=='.' else 0 for c in row]) for row in tiles]))