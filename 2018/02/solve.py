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

def letterwise_and(word1, word2):
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                yield word1[i]

def find_the_two_boxes(box_list):
    for i in range(len(box_list) - 1):
        for j in range(i + 1, len(box_list)):
            common = ''.join(letterwise_and(box_list[i], box_list[j]))
            if len(common) == len(box_list[i]) - 1:
                return common

if __name__ == '__main__':
    with open('input') as f:
        box_list = [l for l in f.readlines()]
    
    print(get_checksum(box_list))

    print(find_the_two_boxes(box_list))