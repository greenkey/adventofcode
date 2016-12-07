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

def ip_supports_ssl(s):
    import re
    buffer = "   "
    inside_brackets = False
    aba_found = list()
    bab_found = list()
    for i in range(len(s)):
        if buffer[0]=='[':
            inside_brackets = True
        if buffer[0]==']':
            inside_brackets = False
        buffer = buffer[1:] + s[i]
        if buffer[0]==buffer[2] and buffer[0]!=buffer[1]:
            if inside_brackets:
                bab_found.append(buffer)
                if buffer[1]+buffer[0]+buffer[1] in aba_found:
                    return True
            if not inside_brackets:
                aba_found.append(buffer)
                if buffer[1]+buffer[0]+buffer[1] in bab_found:
                    return True
    return False

with open(sys.argv[1],'r') as f:
    print("Valids IP count: {}".format(sum([is_valid_ip(l.strip()) for l in f])))
with open(sys.argv[1],'r') as f:
    print("IP supporting SSL: {}".format(sum([ip_supports_ssl(l.strip()) for l in f])))
