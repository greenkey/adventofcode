import re
from collections import Counter

file_name = 'input'

line_pattern = re.compile(r'^([0-9]+)-([0-9]+) (.): (.+)$')
with open(file_name, 'r') as f:
    data = [line_pattern.findall(line)[0] for line in f.readlines()]

first_count = 0
second_count = 0
for nmin, nmax, letter, password in data:
    nmin = int(nmin)
    nmax = int(nmax)
    counted = Counter(password)
    first_count += nmin <= counted[letter] <= nmax

    positions = password[nmin-1] + password[nmax-1]
    second_count += letter in positions and positions != letter * 2

print(first_count)
print(second_count)

