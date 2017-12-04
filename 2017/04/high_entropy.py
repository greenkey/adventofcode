#env python3

with open("input") as f:
    lines = f.readlines()


count = 0

for line in lines:
    words = dict()
    for word in line.strip().split(" "):
        if word in words:
            break
        words[word] = 1
    else:
        count += 1
    
print(count)


count = 0

for line in lines:
    words = dict()
    for word in line.strip().split(" "):
        word = "".join(sorted(list(word)))
        if word in words:
            break
        words[word] = 1
    else:
        count += 1
    
print(count)