import sys

file_name = sys.argv[1:] or 'input'

print(sum(int(line) // 3 - 2 for line in open(file_name).readlines()))