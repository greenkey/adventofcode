from random import randrange


def full_react(polymer):
    polymer = list(polymer)
    i = 0
    while True:
        if i >= len(polymer)-1:
            break

        if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
            del polymer[i+1], polymer[i]
            i = i-1 if i > 0 else 0
            continue
        else:
            i += 1
    return ''.join(polymer)

if __name__ == '__main__':
    with open('input') as f:
        polymer = f.read()
    
    new_polymer = full_react(polymer)
    print(len(new_polymer))

    min_size = len(polymer)
    for l in 'abcdefghijklmnopqrstuvwxyz':
        print('trying with', l)
        new_polymer = polymer.replace(l,'').replace(l.upper(),'')
        new_polymer = full_react(new_polymer)
        min_size = min(len(new_polymer), min_size)

    print(min_size)