from collections import defaultdict

def is_candidate(box_id):
    letter_counts = defaultdict(int)
    for l in box_id:
        letter_counts[l] += 1

    two = len([letter for letter, count in letter_counts.items() if count == 2])
    three = len([letter for letter, count in letter_counts.items() if count == 3])
    return two, three

with open('input') as f:
    twos = 0
    threes = 0
    for box in f.readlines():
        two, three = is_candidate(box)
        twos += bool(two)
        threes += bool(three)

    print(twos*threes)
