from collections import defaultdict
import re

def nodes_are_adjacents(a,b):
	return (a[0]==b[0] and abs(a[1]-b[1])==1) or (a[1]==b[1] and abs(a[0]-b[0])==1)

if __name__ == '__main__':
	fname = 'input'

	grid = dict()

	for l in open(fname):
		if not l.startswith('/dev/grid/node'):
			continue
		(filesystem, size, used, avail, use_perc) = l.split()
		# i.e. /dev/grid/node-x0-y0     93T   67T    26T   72%
		(x,y) = [int(i) for i in list(re.search(r'/dev/grid/node-x(\d+)-y(\d+)',filesystem).groups())]
		grid[(x,y)] = [int(i.replace('T','')) for i in [size, used, avail]]

	viable_nodes = set()
	vals = grid.keys()
	for k1 in grid.keys():
		for k2 in grid.keys():
			if k1==k2:
				continue
			if grid[k1][1] == 0:
				continue
			if grid[k1][1] <= grid[k2][2]:
				viable_nodes.add((k1,k2))
	print(len(viable_nodes))
