
import sys, re

# Part One

def parse_line(line):
	return [int(i) for i in re.split( " +", line.strip() ) ]

def possible_triangle(sides):
	return sum(sides)-max(sides) > max(sides)

with open(sys.argv[1],'r') as f:
	print(sum( [possible_triangle(triangle) for triangle in [parse_line(l) for l in f] ] ))

# Part Two

from functools import reduce

def sum_list(l1,l2):
	return l1+l2

def transpose(l):
	return [list(l) for l in zip(*l)]

def parse_every_three_lines(lines):
	return reduce(sum_list, [transpose(list([parse_line(l) for l in lines[i-2:i+1]])) if (i+1)%3==0 else [] for i in range(len(lines))]) 

with open(sys.argv[1],'r') as f:
	print(sum( [possible_triangle(triangle) for triangle in parse_every_three_lines( f.read().splitlines() ) ] ))
	