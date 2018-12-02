from collections import defaultdict

def is_candidate(box_id):
    letter_counts = defaultdict(int)
    for l in box_id:
        letter_counts[l] += 1

    two = len([letter for letter, count in letter_counts.items() if count == 2])
    three = len([letter for letter, count in letter_counts.items() if count == 3])
    return two, three

def get_checksum(box_list):
    twos = 0
    threes = 0
    for box in box_list:
        two, three = is_candidate(box)
        twos += bool(two)
        threes += bool(three)

    return twos * threes

if __name__ == '__main__':
    with open('input') as f:
        box_list = [l for l in f.readlines()]
    
    print(get_checksum(box_list))
