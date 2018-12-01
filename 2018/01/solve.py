with open('input') as f:
    changes = [int(l) for l in f.readlines()]

freq = 0
freqs = {0,}
i = 0
size = len(changes)

while True:
    freq += changes[i % size]
    if freq in freqs:
        print(freq)
        break
    freqs.add(freq)
    i += 1
