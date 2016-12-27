from collections import defaultdict
import re

def get_near_points(p,grid):
	(x,y) = p
	return set([(x+1,y),(x-1,y),(x,y+1),(x,y-1)]) & set(grid.keys())

def printable_grid(g,max_x=0,max_y=0):
	ret = ''
	if not max_x or not max_y:
		for (x,y) in g.keys():
			max_x = max(max_x,x)
			max_y = max(max_y,y)
	for x in range(max_x+1):
		for y in range(max_y+1):
			ret += g[(x,y)]
		ret += '\n'
	return ret

def find_path(start,end,grid):
	seen_points = set()
	paths = [ [start] ]
	while paths:
		path = paths.pop(0)
		g = path[-1]
		if g == end:
			return path
		for ng in get_near_points(g,grid):
			if ng not in seen_points and grid[ng] not in ['#','G']:
				paths.append( path+[ng] )
				seen_points.add(ng)

def swap_nodes(a,b,grid):
	c = grid[a]
	grid[a] = grid[b]
	grid[b] = c


def free_point(p,grid):
	# find empty
	for start in [p for p in grid.keys() if grid[p]=='_']:
		path = find_path(start,p,grid)
		yield path[:]
		# moves all data
		e = path.pop(0)
		while path:
			n = path.pop(0)
			swap_nodes(e,n,grid)
			e = n
		yield grid



if __name__ == '__main__':
	fname = 'input'

	grid = dict()
	max_x = 0
	max_y = 0

	for l in open(fname):
		if not l.startswith('/dev/grid/node'):
			continue
		(filesystem, size, used, avail, use_perc) = l.split()
		# i.e. /dev/grid/node-x0-y0     93T   67T    26T   72%
		(x,y) = [int(i) for i in list(re.search(r'/dev/grid/node-x(\d+)-y(\d+)',filesystem).groups())]
		grid[(x,y)] = [int(i.replace('T','')) for i in [size, used, avail]]
		(max_x, max_y) = (max(max_x,x), max(max_y,y))

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
	print("Part One:",len(viable_nodes))


	# Part Two

	# printable grid
	new_grid = dict()
	for x in range(max_x+1):
		for y in range(max_y+1):
			if grid[(x,y)][1] == 0: # empty node
				new_grid[(x,y)] = '_'
			elif grid[(x,y)][1] > min([grid[n][0] for n in get_near_points((x,y),grid)]): # too big
				new_grid[(x,y)] = '#'
			else: # has data movable in any direction
				new_grid[(x,y)] = '.'
	grid = new_grid
	printable_grid(grid,max_x,max_y)
	print()

	# find a path for the Goal data to go in 0,0
	#g = (0, max([y for (x,y) in grid.keys()]) )
	g = (max([x for (x,y) in grid.keys()]), 0 )
	grid[g] = 'G'
	g_path = find_path(g,(0,0),grid)

	# count moves to free each step
	moves_no = 0
	new_grid = grid.copy()
	for i in range(len(g_path)-1):
		g = g_path[i]
		p = g_path[i+1]
		(path,new_grid) = free_point(p,new_grid)
		moves_no += len(path)

		# moving G
		swap_nodes(g,p,new_grid)

	print("Part Two:",moves_no)
