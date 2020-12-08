from typing import List


class Intcode:
    def __init__(self, memory: List[int]):
        self.start_memory = memory

    def run(self, noun: int, verb: int) -> int:
        code = self.start_memory[:]
        code[1] = noun
        code[2] = verb

        i = 0
        while code[i] != 99:
            op, op1, op2, dest = code[i : i + 4]
            if op == 1:
                code[dest] = code[op1] + code[op2]
            elif op == 2:
                code[dest] = code[op1] * code[op2]
            else:
                print(f"error, found code {op}")
            i += 4

        return code[0]
