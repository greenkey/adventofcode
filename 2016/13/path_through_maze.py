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

	def find_next_position_from(self,position):
		(x,y) = position
		for (x,y) in [(x+1, y),(x, y+1),(x-1, y),(x, y-1)]:
			if x>=0 and y>=0 and self.is_free_and_new(x, y):
				yield (x,y)

def find_paths(initial_position,position_to_reach,maze):
	paths_so_far = [[initial_position]]
	while paths_so_far:
		p = paths_so_far.pop()
		(x,y) = p[-1]
		for (x,y) in maze.find_next_position_from(p[-1]):
			if (x,y) == position_to_reach:
				return p + [(x,y)]
			paths_so_far.insert(0, p + [(x,y)] )

def find_reachable_locations(initial_position,maze,max_steps):
	paths_so_far = [[initial_position]]
	while paths_so_far:
		p = paths_so_far.pop()
		if len(p) > max_steps:
			continue
		for (x,y) in maze.find_next_position_from(p[-1]):
			paths_so_far.insert(0, p + [(x,y)] )
		

m = Maze(int(sys.argv[1]))
position = (1,1)
position_to_reach = tuple([int(i) for i in sys.argv[2].split(',')])

min_path = None
min_path = find_paths(position,position_to_reach,m)

print("Found path with {} steps:\n{}".format(len(min_path)-1, min_path))

m = Maze(int(sys.argv[1]))
find_reachable_locations(position,m,int(sys.argv[3]))

print("Total number of reached locations: {}".format( sum(m.maze.values()) ))
