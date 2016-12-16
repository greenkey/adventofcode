import sys

class Maze():

	def __init__(self,k):
		self.k = k
		self.maze = dict()
		self.size = (0,0)

	def __repr__(self):
		self.print_with_path(self)

	def print_with_path(self,path=[]):
		out = ' ' + ''.join([str(i)[-1] for i in range(self.size[0])]) + '\n'
		for y in range(self.size[1]):
			out += str(y)[-1]
			for x in range(self.size[0]):
				if (x,y) not in self.maze:
					out += ' '
				elif (x,y) in path:
					out += 'O'
				else:
					out += '.' if self.maze[(x,y)] else '#'
			out += "\n"
		return out

	def calculate_free(self,x,y):
		self.size = (max(self.size[0],x), max(self.size[1],y))
		n = "{0:b}".format(x*x + 3*x + 2*x*y + y + y*y + self.k)
		if sum([int(c) for c in n])%2 == 0:
			return True
		return False
		n = x*x + 3*x + 2*x*y + y + y*y + self.k
		return bin(n)[2:].count('1') % 2 == 0 and x >= 0 and y >= 0

	def is_free(self,x,y):
		try:
			return self.maze[(x,y)]
		except:
			self.maze[(x,y)] = self.calculate_free(x,y)
			return self.maze[(x,y)]

	def is_free_and_new(self,x,y):
		if (x,y) in self.maze.keys():
			return False
		return self.is_free(x,y)

def find_paths(path_so_far,position_to_reach,maze):
	print(maze)
	print(path_so_far[-1],position_to_reach)
	print(path_so_far[-1] == position_to_reach)
	input()
	if path_so_far[-1] == position_to_reach:
		yield path_so_far
	else:
		(x,y) = path_so_far[-1]
		print("current position",x,y)
		next_position = set()
		if maze.is_free_and_new(x+1, y):
			next_position.add((x+1, y))
		if maze.is_free_and_new(x, y+1):
			next_position.add((x, y+1))
		if x > 0 and maze.is_free_and_new(x-1, y):
			next_position.add((x-1, y))
		if y > 0 and maze.is_free_and_new(x, y-1):
			next_position.add((x, y-1))
		print("next positions", next_position)
		for p in next_position:
			for path in find_paths(path_so_far+[(p[0], p[1])], position_to_reach, maze):
				yield path

def find_paths2(initial_position,position_to_reach,maze):
	paths_so_far = [[initial_position]]
	while paths_so_far:
		p = paths_so_far.pop()
		print(maze.print_with_path(p))
		#print(p)
		#input()
		(x,y) = p[-1]
		for (x,y) in [(x+1, y),(x, y+1),(x-1, y),(x, y-1)]:
			if x>=0 and y>=0 and maze.is_free_and_new(x, y):
				if (x,y) == position_to_reach:
					return p + [(x,y)]
				paths_so_far.insert(0, p + [(x,y)] )
		

m = Maze(int(sys.argv[1]))
position = (1,1)
position_to_reach = tuple([int(i) for i in sys.argv[2].split(',')])

min_path = None
#for p in find_paths([position],position_to_reach,m):
#	print("path found: {}".format(p))
#	print(m)
#	if not min_path:
#		min_path = p
#	elif len(min_path) > len(p):
#		min_path = p
min_path = find_paths2(position,position_to_reach,m)

print("Found path with {} steps:\n{}".format(len(min_path)-1, min_path))
