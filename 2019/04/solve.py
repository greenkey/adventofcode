import sys

file_name = sys.argv[1:] or 'input'

start, end = [int(n) for n in open(file_name).read().split('-')]

count = 0
for x in range(start, end + 1):
    sx = str(x)
    if len(set(sx)) == len(sx):
        continue
    if sorted(sx) == list(sx):
        count += 1

print(count)