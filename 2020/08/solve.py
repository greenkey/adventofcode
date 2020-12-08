code = open('input').readlines()

accumulator = 0
current_line = 0
lines_visited = set()

while current_line not in lines_visited:
    lines_visited.add(current_line)
    operation = code[current_line][:3]

    if operation == 'nop':
        current_line += 1
        continue
    argument = int(code[current_line][4:])
    if operation == 'acc':
        accumulator += argument
        current_line += 1
        continue
    elif operation == 'jmp':
        current_line += argument
        continue

print(accumulator)