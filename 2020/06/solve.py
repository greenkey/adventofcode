import string
from collections import Counter

file_name = 'input'
ascii_lowercase = set(string.ascii_lowercase)

with open(file_name, 'r') as f:
    tickets = f.readlines()

data = open(file_name, 'r').read().split('\n\n')

first_count = 0
second_count = 0
for group in data:
    count = Counter(group.strip())
    first_count += len(ascii_lowercase.intersection(count.keys()))
    group_size = len(group.strip().split('\n'))
    second_count += len([question for question, yess in count.items() if yess == group_size])

print(first_count)
print(second_count)