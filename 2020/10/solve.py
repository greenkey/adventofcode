from collections import Counter


def solve(input_file: str):
    adapters = sorted([int(x) for x in open(input_file).readlines()])
    diffs = (
        [adapters[0]]
        + [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
        + [3]
    )
    diff_count = Counter(diffs)
    print(diff_count[1] * diff_count[3])


if __name__ == "__main__":
    solve("input")
