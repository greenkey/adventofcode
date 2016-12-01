import json

first_difference = 0
second_difference = 0

with open("input", "r") as strings:
    for string in strings:
    	string = string.strip()
    	first_difference += len(string) - len( eval(string) )
    	second_difference += len( json.dumps(string) ) - len(string)

print("difference: {}".format( first_difference ))
print("second difference: {}".format( second_difference ))