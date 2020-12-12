from collections import namedtuple
from typing import Callable, Iterable, Optional

import pytest

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


class TestIntcode:
    def test_init(self):
        code = Intcode("10,20,30,40")
        assert code.code == [10, 20, 30, 40]

    def test_get(self):
        code = Intcode("4,3,2,1")
        assert code.get(Operator(1, code.POSITION_MODE)) == 1
        assert code.get(Operator(1, code.IMMEDIATE_MODE)) == 3

    def test_set(self):
        code = Intcode("4,3,2,1,0")

        with pytest.raises(ValueError):
            code.set(Operator(1, code.IMMEDIATE_MODE), 50)
        assert code.code == [4, 3, 2, 1, 0]

        code.set(Operator(1, code.POSITION_MODE), 50)
        assert code.code == [4, 3, 2, 50, 0]

    def test_get_fun(self):
        code = Intcode("99")
        assert code.fun(1) == code._sum
        assert code.fun(2) == code._mul
        assert code.fun(3) == code._input
        assert code.fun(4) == code._output
        assert code.fun(5) == code._jump_if_true
        assert code.fun(6) == code._jump_if_false
        assert code.fun(7) == code._less_than
        assert code.fun(8) == code._equals

    def test_parse_instruction(self):
        result = Intcode.parse_instruction(102)
        assert result.opcode == 2
        assert result.modes == (1, 0, 0)
        assert result == (result.opcode, result.modes)

        assert Intcode.parse_instruction(2) == (2, (0, 0, 0))
        assert Intcode.parse_instruction(11105) == (5, (1, 1, 1))

    def test_sum(self):
        code = Intcode("0001,4,3,4,0,1,0,0")

        # immediate, so sum will be: 4 + 3 -> code[4]
        next_index = code._sum(0, (1, 1, 0))
        assert code.code == [1, 4, 3, 4, 7, 1, 0, 0]
        assert next_index == 4

        # positional, so sum will be: code[3] + code[4] = 4 + 7 -> code[7]
        next_index = code._sum(1, (0, 0, 0))
        assert code.code == [1, 4, 3, 4, 7, 1, 0, 11]
        assert next_index == 5

    def test_mul(self):
        code = Intcode("0001,2,3,3,5,0,7")

        # immediate, so product will be: 2 * 3 -> code[3]
        next_index = code._mul(0, (1, 1, 0))
        assert code.code == [1, 2, 3, 6, 5, 0, 7]
        assert next_index == 4

        # positional, so product will be: code[3] + code[6] = 6 * 7 -> code[5]
        next_index = code._mul(1, (0, 0, 0))
        assert code.code == [1, 2, 3, 6, 5, 42, 7]
        assert next_index == 5

    def test_input(self):
        code = Intcode("003,2,99", input_callback=lambda: "1")

        next_index = code._input(0, (0, 0, 0))
        assert code.code == [3, 2, 1]
        assert next_index == 2

        next_index = code._input(1, (0, 1, 1))
        assert code.code == [3, 1, 1]
        assert next_index == 3

    def test_output(self):
        values = list()
        code = Intcode("004,5,004,1,42,99", output_callback=lambda x: values.append(x))

        next_index = code._output(0, (0, 0, 0))
        assert values == [99]
        assert code.code == [4, 5, 4, 1, 42, 99]
        assert next_index == 2

        next_index = code._output(1, (1, 1, 1))
        assert values == [99, 4]
        assert code.code == [4, 5, 4, 1, 42, 99]
        assert next_index == 3

    def test_jump_if_true(self):
        # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter
        code = Intcode("5,1,3,0")

        next_index = code._jump_if_true(0, (0, 0, 0))
        assert code.code == [5, 1, 3, 0]
        assert next_index == 0

        next_index = code._jump_if_true(1, (0, 0, 0))
        assert code.code == [5, 1, 3, 0]
        assert next_index == 4

    def test_jump_if_false(self):
        # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter
        code = Intcode("6,1,3,0")

        # if code[1] == 0, jump to code[3], else index + 3
        next_index = code._jump_if_false(0, (0, 0, 0))
        assert code.code == [6, 1, 3, 0]
        assert next_index == 3

        # if code[3] == 0, jump to code[0], else index + 3
        next_index = code._jump_if_false(1, (0, 0, 0))
        assert code.code == [6, 1, 3, 0]
        assert next_index == 6

    def test_less_than(self):
        code = Intcode("7,1,0,4,99")

        next_index = code._less_than(0, (0, 0, 0))
        assert code.code == [7, 1, 0, 4, 1]
        assert next_index == 4

        next_index = code._less_than(1, (0, 0, 0))
        assert code.code == [7, 0, 0, 4, 1]
        assert next_index == 5

    def test_equals(self):
        code = Intcode("8,1,0,3,0")

        next_index = code._equals(0, (0, 0, 0))
        assert code.code == [8, 1, 0, 0, 0]
        assert next_index == 4

        next_index = code._equals(1, (0, 0, 0))
        assert code.code == [1, 1, 0, 0, 0]
        assert next_index == 5

    def test_run(self):
        code = Intcode("1002,4,3,4,33")
        code.run()
        assert code.code == [1002, 4, 3, 4, 99]

    def test_run_input_output(self):
        values = list()
        code = Intcode(
            "3,0,4,0,99",
            input_callback=lambda: "1",
            output_callback=lambda x: values.append(x),
        )
        code.run()
        assert code.code == [1, 0, 4, 0, 99]
        assert values == [1]

    @pytest.mark.parametrize(
        "raw_code,input_,output_",
        [
            ("3,9,8,9,10,9,4,9,99,-1,8", 8, 1),  # position mode, equal, true
            ("3,9,8,9,10,9,4,9,99,-1,8", 9, 0),  # position mode, equal, false
            ("3,9,7,9,10,9,4,9,99,-1,8", 8, 0),  # position mode, less, false
            ("3,9,7,9,10,9,4,9,99,-1,8", 7, 1),  # position mode, less, true
            ("3,3,1108,-1,8,3,4,3,99", 8, 1),  # immediate mode, equal, true
            ("3,3,1108,-1,8,3,4,3,99", 9, 0),  # immediate mode, equal, false
            ("3,3,1107,-1,8,3,4,3,99", 8, 0),  # immediate mode, less, false
            ("3,3,1107,-1,8,3,4,3,99", 7, 1),  # immediate mode, less, true
            (
                "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9",
                7,
                1,
            ),  # position mode, is zero, false
            (
                "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9",
                0,
                0,
            ),  # position mode, is zero, true
            (
                "3,3,1105,-1,9,1101,0,0,12,4,12,99,1",
                1,
                1,
            ),  # immediate mode, is zero, false
            (
                "3,3,1105,-1,9,1101,0,0,12,4,12,99,1",
                0,
                0,
            ),  # immediate mode, is zero, true
        ],
    )
    def test_some_other_cases(self, raw_code, input_, output_):
        io = [input_]
        input_callback = lambda: io.pop(0)
        output_callback = lambda x: io.append(x)
        code = Intcode(
            raw_code, input_callback=input_callback, output_callback=output_callback
        )

        code.run()

        assert io == [output_]

    @pytest.mark.parametrize(
        "input_,output_",
        [
            (3, 999),
            (8, 1000),
            (19, 1001),
        ],
    )
    def test_last_case(self, input_, output_):
        io = [input_]
        input_callback = lambda: io.pop(0)
        output_callback = lambda x: io.append(x)
        code = Intcode(
            "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99",
            input_callback=input_callback,
            output_callback=output_callback,
        )

        code.run()

        assert io == [output_]


def solve(file_name: str = "input"):
    code = Intcode(open(file_name).read())
    code.run()


if __name__ == "__main__":
    solve()
