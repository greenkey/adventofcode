import sys

def look_and_say(string,times):
	for i in range(times):
		new_string = ""
		cur_c = ""
		cnt_c = 0
		for c in string:
			if c == cur_c:
				cnt_c += 1
			else:
				if cur_c != "":
					new_string += "{}{}".format(cnt_c,cur_c)
				cur_c = c
				cnt_c = 1
		string = new_string + "{}{}".format(cnt_c,cur_c)
	return string

if __name__ == "__main__":
	las = look_and_say(sys.argv[1],int(sys.argv[2]))
	print("length of the result: {}".format( len(las) ))