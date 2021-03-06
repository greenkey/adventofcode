import sys
from collections import Counter

def solve(file_name: str = "input"):

    start, end = [int(n) for n in open(file_name).read().split('-')]

    passwords = set()
    for x in range(start, end + 1):
        sx = str(x)
        if len(set(sx)) == len(sx):
            continue
        if sorted(sx) == list(sx):
            passwords.add(x)

    print(len(passwords))

    for x in sorted(passwords.copy()):
        counted = Counter(str(x))
        if not any(c == 2 for c in counted.values()):
            passwords.remove(x)

    print(len(passwords))

if __name__ == "__main__":
    solve()
