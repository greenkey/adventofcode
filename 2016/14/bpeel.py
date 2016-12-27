import hashlib
import sys
import re

def get_hash_part1(salt, index):
    m = hashlib.md5()
    m.update(salt.encode("utf-8"))
    m.update(str(index).encode("utf-8"))
    return m.hexdigest()

def get_hash_part2(salt, index):
    h = get_hash_part1(salt, index)

    for i in range(2016):
        h = hashlib.md5(h.encode("utf-8")).hexdigest()

    return h

def find_five_repeats(hashes, ch):
    quintuple = ch * 5

    for h in hashes:
        if h.find(quintuple) != -1:
            return True

    return False    

def solve(salt, get_hash):
    triple = re.compile(r'(.)\1\1')

    hashes = [get_hash(salt, x) for x in range(1001)]

    index = 0
    found = 0

    while True:
        h = hashes.pop(0)
        md = triple.search(h)
        if md and find_five_repeats(hashes, md.group(1)):
            found += 1
            print(index,h)
            #print(' ok')
            if found >= 64:
                break

        index += 1
        hashes.append(get_hash(salt, index + len(hashes)))

    return index

if len(sys.argv) > 1:
    salt = sys.argv[1]
else:
    salt = "abc"

print("Part 1:", solve(salt, get_hash_part1))
#print("Part 2:", solve(salt, get_hash_part2))