import json

def objSum(obj):
	s = 0
	if type(obj) == int:
		return obj
	if type(obj) == list:
		for i in obj:
			s += objSum(i)
	if type(obj) == dict:
		for k,v in obj.items():
			s += objSum(v)
	return s

with open('input', 'r') as content_file:
    obj = json.loads(content_file.read())
print("sum of all numbers: {}".format( objSum(obj) ))
