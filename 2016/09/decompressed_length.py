
# to get the input from a file use the following syntax in *nix:
# python3 decompressed_length.py `cat input`

import sys

def decompress(s):
    decompressed = ""
    i = 0
    while i < len(s):
        if s[i] == "(":
            marker = ""
            while s[i] != ")":
                i += 1
                marker += s[i]
            i += 1
            (characters,times) = [int(_) for _ in marker[:-1].split('x')]
            decompressed += s[i:i+characters] * times
            i += characters
        elif s[i] != " ":
            decompressed += s[i]
            i += 1
    return decompressed

def decompress_v2_count(s):
    count = 0
    i = 0
    while i < len(s):
        if s[i] == "(":
            marker = ""
            while s[i] != ")":
                i += 1
                marker += s[i]
            i += 1
            (characters,times) = [int(_) for _ in marker[:-1].split('x')]
            dec1 = decompress_v2_count(s[i:i+characters])
            count += dec1 * times
            i += characters
        elif s[i] != " ":
            count += 1
            i += 1
    return count


s = decompress(sys.argv[1])
print("Part One: {}".format(len(s)))

print("Part Two: {}".format(decompress_v2_count(s)))
