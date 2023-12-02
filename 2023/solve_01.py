import run

year = 2023
day = 1

example_data_b = '\n'.join([
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
])


def solve_a(data):
    nums = []
    for line in data.splitlines():
        digits = [d for d in line if d in "0123456789"]
        nums.append(int(digits[0]+digits[-1]))
    return sum(nums)


def solve_b(data):
    nums = []
    for line in data.splitlines():
        digits = f"{_first_digit(line)}{_last_digit(line)}"
        n = int(digits)
        nums.append(n)
    return sum(nums)


replacers = {
    "one": 1,
    "1": 1,
    "two": 2,
    "2": 2,
    "three": 3,
    "3": 3,
    "four": 4,
    "4": 4,
    "five": 5,
    "5": 5,
    "six": 6,
    "6": 6,
    "seven": 7,
    "7": 7,
    "eight": 8,
    "8": 8,
    "nine": 9,
    "9": 9,
}


def _first_digit(s: str) -> int:
    max_len = max(len(k) for k in replacers.keys())
    for start in range(len(s)):
        for length in range(max_len):
            word = s[start:start+length+1]
            if word in replacers:
                return replacers[word]


def _last_digit(s: str) -> int:
    max_len = max(len(k) for k in replacers.keys())
    for start in range(len(s)+1, -1, -1):
        for length in range(max_len):
            word = s[start:start+length+1]
            if word in replacers:
                return replacers[word]


run.runme()
