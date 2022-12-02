import solve


class Solution(solve.Solution):
    answer_example_a = 24000
    answer_example_b = 45000

    def get_elves(self):
        elf = 0

        for line in self.data.splitlines():
            if line.strip() == "":
                yield elf
                elf = 0
            else:
                elf += int(line)
        yield elf

    def solve_a(self):
        elves = list(self.get_elves())
        return sorted(elves)[-1]

    def solve_b(self):
        elves = list(self.get_elves())
        return sum(sorted(elves)[-3:])


def test_ciao():
    pass
