character_difference = 0

with open("input", "r") as strings:
    for string in strings:
    	string = string.strip()
    	print("{} is long {}".format(string,len(string)))
    	s2 = eval(string)
    	print("{} is long {}".format(s2,len(s2)))

    	character_difference += len(string) - len( eval(string) )

print("difference: {}".format( character_difference ))