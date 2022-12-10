from time import sleep

import solve

answer_example_a = 13140
answer_example_b = None
example_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


class Screen:
    END = -1

    def __init__(self, data):
        self.x = 1
        self.pointer = 0
        self.pixels = [0] * 241

        self.x_change = {}
        i = 1
        for instruction in data.splitlines():
            match instruction.split():
                case "noop":
                    # i += 1
                    pass
                case "addx", n:
                    i += 1
                    self.x_change[i] = int(n)
            i += 1

    def cycle(self, n: int, show: bool = False):
        if n == self.END:
            n = max(self.x_change.keys()) + 10
        for _ in range(n):
            done = ""
            if x_change := self.x_change.get(self.pointer):
                self.x += x_change
                done = f"finish executing addx {x_change} (Register X is now {self.x})"
            else:
                done = f"nothing happened"
            self.draw()
            self.pointer += 1
            if show:
                self.show()
                sleep(0.05)

    def draw(self):
        if self.pointer % 40 in (self.x - 1, self.x, self.x + 1):
            self.pixels[self.pointer] = 1

    def show(self):
        pixels = "".join("\u2588" if x else " " for x in self.pixels)
        print("-" * 40)
        print(pixels[0:40])
        print(pixels[40:80])
        print(pixels[80:120])
        print(pixels[120:160])
        print(pixels[160:200])
        print(pixels[200:240])
        print("-" * 40)


def solve_a(data):
    screen = Screen(data)
    total_signal_strength = 0
    total_cycles = 0
    for cycle in [20, 40, 40, 40, 40, 40]:
        screen.cycle(cycle)
        total_cycles += cycle
        strength = screen.x * total_cycles
        total_signal_strength += strength
    return total_signal_strength


def solve_b(data):
    screen = Screen(data)
    screen.cycle(screen.END, show=True)
    # screen.show()


def test_simple():
    data = """noop
addx 3
addx -5
"""
    screen = Screen(data)
    screen.cycle(6)
    assert screen.x == -1, screen.x


def test_big():
    data = example_data
    screen = Screen(data)

    screen.cycle(20)
    assert screen.x == 21, screen.x
    screen.cycle(40)  # 60
    assert screen.x == 19, screen.x
    screen.cycle(40)  # 100
    assert screen.x == 18, screen.x
    screen.cycle(40)  # 140
    assert screen.x == 21, screen.x
    screen.cycle(40)  # 180
    assert screen.x == 16, screen.x
    screen.cycle(40)  # 220
    assert screen.x == 18, screen.x


if __name__ == "__main__":
    solve.main(2022, 10)
