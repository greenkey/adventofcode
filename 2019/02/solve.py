import sys

file_name = sys.argv[1:] or 'input'

opcode = [int(n.strip()) for n in open(file_name).read().split(',')]

opcode[1] = 12
opcode[2] = 2

i = 0
while opcode[i] != 99:
    op, op1, op2, dest = opcode[i:i+4]
    if op == 1:
        opcode[dest] = opcode[op1] + opcode[op2]
    elif op == 2:
        opcode[dest] = opcode[op1] * opcode[op2]
    else:
        print(f'error, found code {op}')
    i += 4

print(opcode[0])