
import sys, re

# Part One

def parse_line(line):
	return list(map(int, re.split( " +", line.strip() ) ))

def possible_triangle(sides):
	return sum(sides)-max(sides) > max(sides)

with open(sys.argv[1],'r') as f:
	print(sum( map(possible_triangle, map(parse_line, [l for l in f] ) ) ))

# Part Two

from functools import reduce

def sum_list(l1,l2):
	return l1+l2

def transpose(l):
	return list(map(list, zip(*l)))

def parse_every_three_lines(lines):
	return reduce(sum_list, map(transpose, [list(map(parse_line, lines[i-2:i+1])) if (i+1)%3==0 else [] for i in range(len(lines))]) )

with open(sys.argv[1],'r') as f:
	print(sum(map(possible_triangle, parse_every_three_lines( f.read().splitlines() ) )))
	