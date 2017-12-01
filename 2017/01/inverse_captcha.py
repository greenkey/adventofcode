#env python3

with open("input") as f:
    input_string = f.read()


prev = input_string[-1]
total = 0
for digit in input_string:
    if digit == prev:
        total += int(digit)
    prev = digit
print(total)

halfway = int(len(input_string) / 2)

total = 0
for i in range(len(input_string)):
    if input_string[i] == input_string[(i + halfway) % len(input_string)]:
        total += int(input_string[i])
print(total)