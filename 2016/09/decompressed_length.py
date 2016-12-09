
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


s = decompress(sys.argv[1])
print("Decompressed string: {} (length: {})".format(s, len(s)))
