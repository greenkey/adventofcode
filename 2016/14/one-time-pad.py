from collections import defaultdict
from hashlib import md5 as sys_md5

class MD5(defaultdict):
	def __missing__(self,key):
		return sys_md5(key.encode()).hexdigest()	

if __name__ == '__main__':
	import sys
	import re

	salt = sys.argv[1]

	pad_keys = list()
	my_md5 = MD5()

	i = 0
	while len(pad_keys)<64:
		h = my_md5[ salt + str(i) ]
		three = re.search(r'(.)\1\1',h)
		if three:
			c = three.group(1)
			for j in range(1,1001):
				if c*5 in my_md5[ salt + str(i+j) ]:
					pad_keys.append((i, h, c, i+j))
					break
		i += 1

	print(pad_keys[-1])