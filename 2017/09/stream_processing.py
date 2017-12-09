import fileinput


def get_stream_score(s):
    level, score, removed = 0, 0, 0
    skip, garbage = False, False

    for c in s:
        if skip:
            skip = False
            continue

        if c == '!':
            skip = True
            continue

        if c == ">":
            garbage = False
        if garbage:
            removed += 1
            continue
        if c == '<':
            garbage = True

        if c == '{':
            level += 1
        if c == '}':
            score += level
            level -= 1
    
    return score, removed

if __name__ == '__main__':
    for line in fileinput.input():
        print(get_stream_score(line))

