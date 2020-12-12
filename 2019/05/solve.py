from collections import namedtuple
from typing import Callable, Iterable, Optional

import pytest

Instruction = namedtuple('Instruction', 'opcode,modes')
Operator = namedtuple('Operator', 'index,mode')


class Intcode:
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    def __init__(self, raw_code: str, input_callback: Optional[Callable] = None, output_callback: Optional[Callable] = None):
        self.code = list(map(int, raw_code.split(',')))
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
            99: lambda *args: -1,
        }[opcode]

    @classmethod
    def parse_instruction(cls, instruction: int) -> Instruction:
        instr = f'00000{instruction}'[-5:]
        opcode = int(instr[-2:])
        modes = tuple(int(x) for x in instr[2::-1])
        return Instruction(opcode, modes)

    def _sum(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        dest = Operator(index + 3, modes[2])
        self.set(dest, self.get(op1) + self.get(op2))
        return index + 4

    def _mul(self, index: int, modes: Iterable[int]) -> int:
        op1 = Operator(index + 1, modes[0])
        op2 = Operator(index + 2, modes[1])
        dest = Operator(index + 3, modes[2])
        self.set(dest, self.get(op1) * self.get(op2))
        return index + 4

    def _input(self, index: int, modes: Iterable[int]) -> int:
        dest = Operator(index + 1, modes[0])
        self.set(dest, int(self.get_input()))
        return index + 2

    def _output(self, index: int, modes: Iterable[int]) -> int:
        source = Operator(index + 1, modes[0])
        self.put_output(self.get(source))
        return index + 2

    def run(self):
        index = 0
        while index >= 0:
            opcode, modes = self.parse_instruction(self.code[index])
            fun = self.fun(opcode)
            index = fun(index, modes)


class TestIntcode:
    def test_init(self):
        code = Intcode('10,20,30,40')
        assert code.code == [10, 20, 30, 40]

    def test_get(self):
        code = Intcode('4,3,2,1')
        assert code.get(Operator(1, code.POSITION_MODE)) == 1
        assert code.get(Operator(1, code.IMMEDIATE_MODE)) == 3

    def test_set(self):
        code = Intcode('4,3,2,1,0')

        with pytest.raises(ValueError):
            code.set(Operator(1, code.IMMEDIATE_MODE), 50)
        assert code.code == [4, 3, 2, 1, 0]

        code.set(Operator(1, code.POSITION_MODE), 50)
        assert code.code == [4, 3, 2, 50, 0]

    def test_get_fun(self):
        code = Intcode('99')
        assert code.fun(1) == code._sum
        assert code.fun(2) == code._mul
        assert code.fun(3) == code._input
        assert code.fun(4) == code._output

    def test_parse_instruction(self):
        result = Intcode.parse_instruction(102)
        assert result.opcode == 2
        assert result.modes == (1, 0, 0)
        assert result == (result.opcode, result.modes)

        assert Intcode.parse_instruction(2) == (2, (0, 0, 0))
        assert Intcode.parse_instruction(11105) == (5, (1, 1, 1))

    def test_sum(self):
        code = Intcode('0001,4,3,4,0,1,0,0')

        # immediate, so sum will be: 4 + 3 -> code[4]
        next_index = code._sum(0, (1, 1, 0))
        assert code.code == [1, 4, 3, 4, 7, 1, 0, 0]
        assert next_index == 4

        # positional, so sum will be: code[3] + code[4] = 4 + 7 -> code[7]
        next_index = code._sum(1, (0, 0, 0))
        assert code.code == [1, 4, 3, 4, 7, 1, 0, 11]
        assert next_index == 5

    def test_mul(self):
        code = Intcode('0001,2,3,3,5,0,7')

        # immediate, so product will be: 2 * 3 -> code[3]
        next_index = code._mul(0, (1, 1, 0))
        assert code.code == [1, 2, 3, 6, 5, 0, 7]
        assert next_index == 4

        # positional, so product will be: code[3] + code[6] = 6 * 7 -> code[5]
        next_index = code._mul(1, (0, 0, 0))
        assert code.code == [1, 2, 3, 6, 5, 42, 7]
        assert next_index == 5

    def test_input(self):
        code = Intcode('003,2,99', input_callback=lambda: '1')

        next_index = code._input(0, (0, 0, 0))
        assert code.code == [3, 2, 1]
        assert next_index == 2

        next_index = code._input(1, (0, 1, 1))
        assert code.code == [3, 1, 1]
        assert next_index == 3

    def test_output(self):
        values = list()
        code = Intcode('004,5,004,1,42,99', output_callback=lambda x: values.append(x))

        next_index = code._output(0, (0, 0, 0))
        assert values == [99]
        assert code.code == [4, 5, 4, 1, 42, 99]
        assert next_index == 2

        next_index = code._output(1, (1, 1, 1))
        assert values == [99, 4]
        assert code.code == [4, 5, 4, 1, 42, 99]
        assert next_index == 3

    def test_run(self):
        code = Intcode('1002,4,3,4,33')
        code.run()
        assert code.code == [1002, 4, 3, 4, 99]

    def test_run_input_output(self):
        values = list()
        code = Intcode('3,0,4,0,99', input_callback=lambda: '1', output_callback=lambda x: values.append(x))
        code.run()
        assert code.code == [1, 0, 4, 0, 99]
        assert values == [1]


def solve(file_name: str = "input"):
    code = Intcode(open(file_name).read())
    code.run()


if __name__ == "__main__":
    solve()
