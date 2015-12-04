import sys
import hashlib

inputString = sys.argv[1]

i = 0

while hashlib.md5(inputString + str(i)).hexdigest()[:5] != "00000":
	i += 1

print( "First number for Santa: {}".format(i) )

while hashlib.md5(inputString + str(i)).hexdigest()[:6] != "000000":
	i += 1

print( "Second number for Santa: {}".format(i) )