import sys
from collections import namedtuple
from itertools import permutations
from typing import Callable, Iterable, Optional, Tuple, List, Any
from day_05 import Instruction, Operator, Intcode


class Intcode2(Intcode):
    def __init__(
        self,
        raw_code: str,
        input_list: Optional[List[Any]] = None,
        output_list: Optional[List[Any]] = None,
    ):
        self.code = list(map(int, raw_code.split(",")))
        self.inputs = [] if input_list is None else input_list
        self.outputs = [] if output_list is None else output_list
        self.index = 0

    def _input(self, index: int, modes: Iterable[int]) -> int:
        dest = Operator(index + 1, modes[0])
        value = self.inputs.pop()
        self.set(dest, int(value))
        return index + 2

    def _output(self, index: int, modes: Iterable[int]) -> int:
        source = Operator(index + 1, modes[0])
        self.outputs.append(self.get(source))
        return index + 2

    def step(self):
        opcode, modes = self.parse_instruction(self.code[self.index])
        fun = self.fun(opcode)
        self.index = fun(self.index, modes)

    def run(self):
        while self.index >= 0:
            self.step()




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


def test_cfg2(code: str, settings: Tuple[int]) -> int:
    prev_outputs = [0]
    last_output = None

    # setup
    amps = list()
    while True:
        for i, cfg in enumerate(settings):

            try:
                amp = amps[i]
            except IndexError:
                amp = Intcode2(code, input_list=prev_outputs)
                amps.append(amp)
                amp.inputs.append(cfg)

            try:
                amp.run()
            except IndexError:
                continue
            else:
                print(settings)
                return last_output
            finally:
                prev_outputs = amp.outputs

        last_output = amps[-1].outputs[-1]
        amps[0].inputs = amps[-1].outputs


def solve(file_name: str = "input"):
    code = open(file_name).read()

    # max_signal = 0
    # best_settings = None
    # for settings in permutations(range(5), r=5):
    #     signal = test_cfg(code, settings)
    #     if signal > max_signal:
    #         max_signal = signal
    #         best_settings = settings
    # print(best_settings, max_signal)

    print(max(test_cfg2(code, settings) for settings in permutations(range(5,10), r=5)))


if __name__ == "__main__":
    filename = f"default.input"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    solve(filename)

