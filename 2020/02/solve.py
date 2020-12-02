import re
from collections import Counter

file_name = 'input'

line_pattern = re.compile(r'^([0-9]+)-([0-9]+) (.): (.+)$')
with open(file_name, 'r') as f:
    data = [line_pattern.findall(line)[0] for line in f.readlines()]

count = 0
for nmin, nmax, letter, password in data:
    counted = Counter(password)
    count += int(nmin) <= counted[letter] <= int(nmax)
print(count)
