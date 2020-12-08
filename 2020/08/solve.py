initial_code = open('input').readlines()

def run_code(code):
    accumulator = 0
    current_line = 0
    previous_line = None
    lines_visited = set()
    exit_status = None
    while True:
        if current_line in lines_visited:
            exit_status = 'loop'
            break
        previous_line = current_line
        lines_visited.add(current_line)
        try:
            operation, argument = code[current_line].split()
        except IndexError:
            exit_status = 'out_of_code'
            break
        argument = int(argument)

        accumulator += argument if operation == 'acc' else 0

        current_line += argument if operation == 'jmp' else 1
    return exit_status, accumulator, previous_line

print(run_code(initial_code)[1])

for i, instruction in enumerate(initial_code):
    operation, argument = instruction.split()
    new_code = initial_code[:]
    if operation == 'jmp':
        new_code[i] = f'nop {argument}'
    elif operation == 'nop':
        new_code[i] = f'jmp {argument}'
    else:
        continue
    exit_status, accumulator, previous_line = run_code(new_code)
    if exit_status == 'out_of_code':
        print(accumulator)
        break
