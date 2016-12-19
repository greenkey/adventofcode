
def next_tile_row_old(row):
	row = [1] + row + [1]
	for i in range(1,len(row)-1):
		yield row[i-1]!=row[i+1]

def next_tile_row(row):
	prev2 = 1
	prev1 = row[0]
	for x in row[1:]:
		yield prev2!=x
		prev2 = prev1
		prev1 = x
	yield prev2!=1


if __name__ == '__main__':

	import sys

	try:
		row = open(sys.argv[1]).read().strip()
	except:
		row = sys.argv[1]

	row = [1 if c=='.' else 0 for c in row]

	count_free = sum(row)
	for i in range(int(sys.argv[2])-1):
		print('\r{} '.format(i), end='')
		row = list(next_tile_row(row))
		count_free += sum(row)

	#print('\n'.join(tiles))
	print(count_free)