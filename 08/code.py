import json

first_difference = 0
second_difference = 0

with open("input", "r") as strings:
    for string in strings:
    	string = string.strip()
    	print("\n{} is long {}".format(string,len(string)))
    	s2 = eval(string)
    	print("{} is long {}".format(s2,len(s2)))
    	s3 = json.dumps(string)
    	print("{} is long {}".format(s3,len(s3)))

    	first_difference += len(string) - len( eval(string) )
    	second_difference += len( json.dumps(string) ) - len(string)

print("\ndifference: {}".format( first_difference ))
print("second difference: {}".format( second_difference ))