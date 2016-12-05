
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

def find_password2(door):
	password = list("        ")
	i = 0
	while sum([0 if c==' ' else 1 for c in password]) < 8:
		current_hash = my_md5(door+str(i))
		if current_hash.startswith("00000"):
			try:
				position = int(current_hash[5])
				if password[position] == ' ':
					character = current_hash[6]
					password[position] = character
					print("password so far: {} - i={} - hash={}".format(''.join(password), i, current_hash))
			except:
				pass
		i += 1
	return ''.join(password)

print(find_password2(sys.argv[1]))