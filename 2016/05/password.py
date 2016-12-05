
import sys

def my_md5(s):
	from hashlib import md5
	return md5(s.encode()).hexdigest()

def find_password(door):
	password = ""
	i = 0
	while len(password) < 8:
		current_hash = my_md5(door+str(i))
		if current_hash.startswith("00000"):
			password += current_hash[5]
			print("password so far: {} - i={} - hash={}".format(password, i, current_hash))
		i += 1
	return password

print(find_password(sys.argv[1]))