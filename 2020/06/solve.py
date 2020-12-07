import string
from collections import Counter

file_name = 'input'
ascii_lowercase = set(string.ascii_lowercase)

with open(file_name, 'r') as f:
    tickets = f.readlines()

data = open(file_name, 'r').read().split('\n\n')

global_count = 0
for group in data:
    count = Counter(group)
    global_count += len(ascii_lowercase.intersection(count.keys()))

print(global_count)