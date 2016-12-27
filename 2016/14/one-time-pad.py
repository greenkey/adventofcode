from collections import defaultdict
from hashlib import md5 as sys_md5

def md5(s):
	return sys_md5(s.encode()).hexdigest()

if __name__ == '__main__':
	import sys
	import re

	salt = sys.argv[1]
	stretch = 0
	if len(sys.argv)>2:
		stretch = int(sys.argv[2])

	pad_keys = list()
	myre = re.compile(r'(.)\1\1')

	def md5_stretched(s,times):
		for _ in range(times):
			s = md5(s)
		return s

	hashes = [md5_stretched( salt + str(i), stretch+1 ) for i in range(1001)]

	i = 0
	while len(pad_keys)<64:
		h = hashes.pop(0)
		three = myre.search(h)
		if three:
			c = three.group(1)
			#print(i, h)
			for j in range(1000):
				if c*5 in hashes[j]:
					print(i, h, c, i+j )
					pad_keys.append((i, h, c, i+j))
					break
		i += 1
		hashes.append( md5_stretched( salt + str(i+1000), stretch+1 ) )

	print(pad_keys[-1])
