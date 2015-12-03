

with open("input", "r") as all_instructions:
	for instructions in all_instructions:

		# first year

		visited_houses = set()
		pos = [0,0]
		visited_houses.add(":".join(map(lambda x: str(x), pos)))

		for direction in instructions:
			if direction == "^":
				pos = [pos[0], pos[1]+1]
			elif direction == ">":
				pos = [pos[0]+1, pos[1]]
			elif direction == "v":
				pos = [pos[0], pos[1]-1]
			elif direction == "<":
				pos = [pos[0]-1, pos[1]]

			visited_houses.add(":".join(map(lambda x: str(x), pos)))

		print("Houses visited the first year: {}".format(len(visited_houses)))

		# second year
		
		visited_houses = set()
		pos = [[0,0],[0,0]]
		visited_houses.add(":".join(map(lambda x: str(x), pos[0])))

		for i in range(len(instructions)):
			direction = instructions[i]
			if direction == "^":
				pos[i%2] = [pos[i%2][0], pos[i%2][1]+1]
			elif direction == ">":
				pos[i%2] = [pos[i%2][0]+1, pos[i%2][1]]
			elif direction == "v":
				pos[i%2] = [pos[i%2][0], pos[i%2][1]-1]
			elif direction == "<":
				pos[i%2] = [pos[i%2][0]-1, pos[i%2][1]]
			visited_houses.add(":".join(map(lambda x: str(x), pos[i%2])))

		print("Houses visited the second year: {}".format(len(visited_houses)))
