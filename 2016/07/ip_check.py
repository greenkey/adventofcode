import sys

def is_valid_ip(s):
    buffer = "    "
    inside_brackets = False
    valid = False
    for c in s:
        if buffer[0]=='[':
            inside_brackets = True
        if buffer[0]==']':
            inside_brackets = False
        buffer = buffer[1:] + c
        if inside_brackets and buffer[0]==buffer[3] and buffer[1]==buffer[2] and buffer[0]!=buffer[1]:
            return False
        if not inside_brackets and buffer[0]==buffer[3] and buffer[1]==buffer[2] and buffer[0]!=buffer[1]:
            valid = True
    return valid

with open(sys.argv[1],'r') as f:
    print("Valids IP count: {}".format(sum([is_valid_ip(l.strip()) for l in f])))
