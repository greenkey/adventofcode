import re

class Scrambler():

	def __init__(self):
		self.rules = list()

	def add_rule(self,rule):
		if rule.startswith('swap position'):
			(x, y) = [int(i) for i in re.search(r'swap position (\d+) with position (\d+)',rule).groups()]
			self.rules.append( lambda s: swap_position(s,x,y) )

		elif rule.startswith('swap letter'):
			(x, y) = re.search(r'swap letter (.) with letter (.)',rule).groups()
			self.rules.append( lambda s: swap_letter(s,x,y) )

		elif rule.startswith('rotate based on position of letter'):
			x = re.search(r'rotate based on position of letter (.)',rule).group(1)
			self.rules.append( lambda s: rotate_dynamic(s,x) )

		elif rule.startswith('rotate'):
			(d,x) = re.search(r'rotate (left|right) (\d+) step',rule).groups()
			self.rules.append( lambda s: rotate_simple(s,d,int(x)) )
		
		elif rule.startswith('reverse positions'):
			(x,y) = [int(i) for i in re.search(r'reverse positions (\d+) through (\d+)',rule).groups()]
			self.rules.append( lambda s: reverse_positions(s,x,y) )
		
		elif rule.startswith('move position'):
			(x,y) = [int(i) for i in re.search(r'move position (\d+) to position (\d+)',rule).groups()]
			self.rules.append( lambda s: move_letters(s,x,y) )

	def scramble(self,s):
		for r in self.rules:
			s = r(s)
		return s

def swap_position(s,x,y):
	''' swap position X with position Y means that the letters at indexes X and
		Y (counting from 0) should be swapped.
	'''
	s = list(s)
	tmp = s[x]
	s[x] = s[y]
	s[y] = tmp
	return ''.join(s)

def swap_letter(s,x,y):
	''' swap letter X with letter Y means that the letters X and Y should be
		swapped (regardless of where they appear in the string).
		i.e. swap letter d with letter b
	'''
	return s.replace(y,'_').replace(x,y).replace('_',x)

def rotate_simple(s,direction,steps):
	''' rotate left/right X steps means that the whole string should be rotated;
		for example, one right rotation would turn abcd into dabc.
 		i.e. rotate left 1 step
	'''
	steps = steps % len(s)
	if direction == 'right':
		steps = -steps
	return s[steps:] + s[:steps]

def rotate_dynamic(s,x):
	''' rotate based on position of letter X means that the whole string should
		be rotated to the right based on the index of letter X (counting from 0)
		as determined before this instruction does any rotations. Once the index
		is determined, rotate the string to the right one time, plus a number of
		times equal to that index, plus one additional time if the index was at
		least 4.
		i.e. rotate based on position of letter d
	'''
	return rotate_simple(s,'right', s.index(x)+1 + (1 if s.index(x)>=4 else 0) )

def reverse_positions(s,x,y):
	''' reverse positions X through Y means that the span of letters at indexes
		X through Y (including the letters at X and Y) should be reversed in
		order.
		i.e. reverse positions 0 through 4
	'''
	return s[:x] + s[x:y+1][::-1] + s[y+1:]

def move_letters(s,x,y):
	''' move position X to position Y means that the letter which is at index X
		should be removed from the string, then inserted such that it ends up at
		index Y.
		i.e. move position 1 to position 4
	'''
	s = list(s)
	l = s.pop(x)
	s.insert(y,l)
	return ''.join(s)

if __name__ == '__main__':
	import sys

	input_s = sys.argv[1]

	if len(sys.argv) > 2:
		fname = sys.argv[2]
	else:
		fname = 'input'

	s = Scrambler()

	[s.add_rule(l.strip()) for l in open(fname)]

	print(s.scramble(input_s))