import re
from collections import defaultdict

file_name = 'input'
bag_content_mask = re.compile(r'([0-9]+) ([^,\.]+) bags?[,\.]')

def parse_line(line):
    root, contains = line.split(' bags contain ')
    contains = [(int(n), desc) for n, desc in bag_content_mask.findall(contains)]
    return root, contains

data = map(parse_line, open(file_name, 'r').readlines())

reverse_tree = defaultdict(dict)
for root, contains in data:
    for n, desc in contains:
        reverse_tree[desc][root] = n

def can_contain(tree):
    for key in tree.keys():
        yield key
        yield from can_contain(reverse_tree[key])

print(len(set(can_contain(reverse_tree['shiny gold']))))
