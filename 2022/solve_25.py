import solve

answer_example_a = "2=-1=0"
answer_example_b = None


class SNAFU:
    _cd = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2,
    }
    _dc = {
        2: "2",
        1: "1",
        0: "0",
        -1: "-",
        -2: "=",
    }

    def __init__(self, value) -> None:
        self.value = value

    @classmethod
    def from_int(cls, n: int) -> "SNAFU":
        digits = []
        while n:
            n += 2
            digits.append(cls._dc[(n % 5) - 2])
            n = n // 5
        return cls("".join(digits[::-1]))

    def to_int(self) -> int:
        int_value = 0
        for i, c in enumerate(self.value[::-1]):
            int_value += 5**i * self._cd[c]
        return int_value

    def __eq__(self, other: "SNAFU") -> bool:
        return self.value == other.value

    def __add__(self, other: "SNAFU") -> "SNAFU":
        return self.from_int(self.to_int() + other.to_int())

    def __str__(self):
        return self.value


def test_snafu_from_int():
    assert SNAFU.from_int(1) == SNAFU("1")
    assert SNAFU.from_int(2) == SNAFU("2")
    assert SNAFU.from_int(3) == SNAFU("1=")
    assert SNAFU.from_int(4) == SNAFU("1-")
    assert SNAFU.from_int(5) == SNAFU("10")
    assert SNAFU.from_int(6) == SNAFU("11")
    assert SNAFU.from_int(7) == SNAFU("12")
    assert SNAFU.from_int(8) == SNAFU("2=")
    assert SNAFU.from_int(9) == SNAFU("2-")
    assert SNAFU.from_int(10) == SNAFU("20")
    assert SNAFU.from_int(15) == SNAFU("1=0")
    assert SNAFU.from_int(20) == SNAFU("1-0")
    assert SNAFU.from_int(2022) == SNAFU("1=11-2")
    assert SNAFU.from_int(12345) == SNAFU("1-0---0")
    assert SNAFU.from_int(314159265) == SNAFU("1121-1110-1=0")
    assert SNAFU.from_int(1747) == SNAFU("1=-0-2")
    assert SNAFU.from_int(906) == SNAFU("12111")
    assert SNAFU.from_int(198) == SNAFU("2=0=")
    assert SNAFU.from_int(11) == SNAFU("21")
    assert SNAFU.from_int(201) == SNAFU("2=01")
    assert SNAFU.from_int(31) == SNAFU("111")
    assert SNAFU.from_int(1257) == SNAFU("20012")
    assert SNAFU.from_int(32) == SNAFU("112")
    assert SNAFU.from_int(353) == SNAFU("1=-1=")
    assert SNAFU.from_int(107) == SNAFU("1-12")
    assert SNAFU.from_int(7) == SNAFU("12")
    assert SNAFU.from_int(3) == SNAFU("1=")
    assert SNAFU.from_int(37) == SNAFU("122")


def test_snafu_to_dec():
    assert SNAFU("1").to_int() == 1
    assert SNAFU("2").to_int() == 2
    assert SNAFU("1=").to_int() == 3
    assert SNAFU("1-").to_int() == 4
    assert SNAFU("10").to_int() == 5
    assert SNAFU("11").to_int() == 6
    assert SNAFU("12").to_int() == 7
    assert SNAFU("2=").to_int() == 8
    assert SNAFU("2-").to_int() == 9
    assert SNAFU("20").to_int() == 10
    assert SNAFU("1=0").to_int() == 15
    assert SNAFU("1-0").to_int() == 20
    assert SNAFU("1=11-2").to_int() == 2022
    assert SNAFU("1-0---0").to_int() == 12345
    assert SNAFU("1121-1110-1=0").to_int() == 314159265
    assert SNAFU("1=-0-2").to_int() == 1747
    assert SNAFU("12111").to_int() == 906
    assert SNAFU("2=0=").to_int() == 198
    assert SNAFU("21").to_int() == 11
    assert SNAFU("2=01").to_int() == 201
    assert SNAFU("111").to_int() == 31
    assert SNAFU("20012").to_int() == 1257
    assert SNAFU("112").to_int() == 32
    assert SNAFU("1=-1=").to_int() == 353
    assert SNAFU("1-12").to_int() == 107
    assert SNAFU("12").to_int() == 7
    assert SNAFU("1=").to_int() == 3
    assert SNAFU("122").to_int() == 37


def test_snafu_sum():
    assert SNAFU("1") + SNAFU("1") == SNAFU("2")
    assert SNAFU("1") + SNAFU("2") == SNAFU("1=")
    assert SNAFU("10") + SNAFU("11") == SNAFU("21")


def solve_a(data):
    total = SNAFU.from_int(0)
    for line in data.splitlines():
        total += SNAFU(line)
    return str(total)


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 25)
