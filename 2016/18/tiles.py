
def next_tile_row(row):
	row = [1] + row + [1]
	ret = []
	for i in range(1,len(row)-1):
		if row[i-1]!=row[i+1]:
			ret.append(0)
		else:
			ret.append(1)
	return ret


if __name__ == '__main__':

	import sys

	try:
		row = open(sys.argv[1]).read().strip()
	except:
		row = sys.argv[1]

	row = [1 if c=='.' else 0 for c in row]

	count_free = sum(row)
	for i in range(int(sys.argv[2])-1):
		row = next_tile_row(row)
		count_free += sum(row)

	#print('\n'.join(tiles))
	print(count_free)