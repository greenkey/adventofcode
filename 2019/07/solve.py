from collections import namedtuple
from itertools import permutations
from typing import Callable, Iterable, Optional, Tuple

Instruction = namedtuple("Instruction", "opcode,modes")
Operator = namedtuple("Operator", "index,mode")


class Intcode:
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    def __init__(
        self,
        raw_code: str,
        input_callback: Optional[Callable] = None,
        output_callback: Optional[Callable] = None,
    ):
        self.code = list(map(int, raw_code.split(",")))
        self.get_input = input_callback or input
        self.put_output = output_callback or print

    def get(self, operator: Operator) -> int:
        num = self.code[operator.index]
        if operator.mode == self.POSITION_MODE:
            return self.code[num]
        elif operator.mode == self.IMMEDIATE_MODE:
            return num
        raise KeyError(operator.mode)

    def set(self, operator: Operator, value: int):
        num = self.code[operator.index]
        if operator.mode != self.POSITION_MODE:
            raise ValueError
        self.code[num] = value

    def fun(self, opcode: int) -> Callable:
        return {
            1: self._sum,
            2: self._mul,
            3: self._input,
            4: self._output,
            5: self._jump_if_true,
            6: self._jump_if_false,
            7: self._less_than,
            8: self._equals,
            99: lambda *args: -1,
        }[opcode]

    @classmethod
    def parse_instruction(cls, instruction: int) -> Instruction:
        instr = f"00000{instruction}"[-5:]
        opcode = int(instr[-2:])
        modes = tuple(int(x) for x in instr[2::-1])
        return Instruction(opcode, modes)

    def op(self, op: Operator) -> str:
        return f"{self.get(op)}@{self.code[op.index]}"

    def _sum(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        dest = Operator(index + 3, modes[2])
        result = self.get(op1) + self.get(op2)
        self.set(dest, result)
        return index + 4

    def _mul(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        dest = Operator(index + 3, modes[2])
        self.set(dest, self.get(op1) * self.get(op2))
        return index + 4

    def _input(self, index: int, modes: Iterable[int]) -> int:
        dest = Operator(index + 1, modes[0])
        value = self.get_input()
        self.set(dest, int(value))
        return index + 2

    def _output(self, index: int, modes: Iterable[int]) -> int:
        source = Operator(index + 1, modes[0])
        self.put_output(self.get(source))
        return index + 2

    def _jump_if_true(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        if self.get(op1):
            return self.get(op2)
        return index + 3

    def _jump_if_false(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        if self.get(op1) == 0:
            return self.get(op2)
        return index + 3

    def _less_than(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        dest = Operator(index + 3, modes[2])
        self.set(dest, int(self.get(op1) < self.get(op2)))
        return index + 4

    def _equals(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        dest = Operator(index + 3, modes[2])
        self.set(dest, int(self.get(op1) == self.get(op2)))
        return index + 4

    def run(self):
        index = 0
        while index >= 0:
            opcode, modes = self.parse_instruction(self.code[index])
            fun = self.fun(opcode)
            index = fun(index, modes)


def test_cfg(code: str, settings: Tuple[int]) -> int:
    signal = 0
    for cfg in settings:
        inputs = [signal, cfg]
        outputs = list()
        amp = Intcode(
            code,
            input_callback=lambda: inputs.pop(),
            output_callback=lambda x: outputs.append(x),
        )
        amp.run()
        signal = outputs.pop()
    return signal


def solve(file_name: str = "input"):
    code = open(file_name).read()

    max_signal = 0
    best_settings = None
    for settings in permutations(range(5), r=5):
        signal = test_cfg(code, settings)
        if signal > max_signal:
            max_signal = signal
            best_settings = settings
    print(best_settings, max_signal)


if __name__ == "__main__":
    solve()
