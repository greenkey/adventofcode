import sys
from typing import List

file_name = sys.argv[1:] or 'input'


class Opcode:
    def __init__(self, memory: List[int]):
        self.start_memory = memory

    def run(self, noun: int, verb: int) -> int:
        code = self.start_memory[:]
        code[1] = noun
        code[2] = verb

        i = 0
        while code[i] != 99:
            op, op1, op2, dest = code[i:i+4]
            if op == 1:
                code[dest] = code[op1] + code[op2]
            elif op == 2:
                code[dest] = code[op1] * code[op2]
            else:
                print(f'error, found code {op}')
            i += 4

        return code[0]


opcode = Opcode([int(n.strip()) for n in open(file_name).read().split(',')])

print(opcode.run(12, 2))

for noun in range(100):
    for verb in range(100):
        result = opcode.run(noun, verb)
        if result == 19690720:
            print(100 * noun + verb)
            break
