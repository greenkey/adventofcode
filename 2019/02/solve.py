from common import Intcode


def solve(file_name: str = "input"):
    opcode = Intcode([int(n.strip()) for n in open(file_name).read().split(",")])

    print(opcode.run(12, 2))

    for noun in range(100):
        for verb in range(100):
            result = opcode.run(noun, verb)
            if result == 19690720:
                print(100 * noun + verb)
                break


if __name__ == "__main__":
    solve()
