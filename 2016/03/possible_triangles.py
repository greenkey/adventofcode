
import sys, re

def parse_line(line):
	return list(map(int, re.split( " +", line.strip() ) ))

def possible_triangle(sides):
	return sum(sides)-max(sides) > max(sides)

f = open(sys.argv[1],'r')
print(sum( map(possible_triangle, map(parse_line, [l for l in f] ) ) ))
