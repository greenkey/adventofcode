
import sys

def get_message_from_stream(f):
	counter_template = [0 for i in range(ord('a'),ord('z')+1)]
	counter = list()
	for l in f:
		for c in range(len(l.strip())):
			try:
				counter[c][ord(l[c])-ord('a')] += 1
			except IndexError:
				counter.append(counter_template[:])
				counter[c][ord(l[c])-ord('a')] += 1
	s1 = ''
	s2 = ''
	for c in range(len(counter)):
		s1 += chr(counter[c].index(max(counter[c]))+ord('a'))
		s2 += chr(counter[c].index(min(counter[c]))+ord('a'))
	return (s1,s2)

with open(sys.argv[1],'r') as f:
	print(get_message_from_stream(f))
