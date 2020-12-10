import sys
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

    arrangements = set(tuple(l) for l in get_arrangements(diffs))
    print(len(arrangements))
    arrangements = list(get_arrangements_first([0] + adapters + [adapters[-1] + 3]))
    print(len(arrangements))


def get_arrangements(diffs, prepend=None):
    prepend = prepend or []
    if not diffs:
        return prepend
    yield prepend + diffs
    yield from get_arrangements(diffs[1:], prepend + [diffs[0]])
    if diffs[:2] == [1, 1]:
        yield from get_arrangements([2] + diffs[2:], prepend)
    if diffs[:2] in ([2, 1], [1, 2]):
        yield from get_arrangements(diffs[2:], prepend + [3])


def get_arrangements_first(adapters, start=0):
    if not adapters:
        return None
    for jump in (1, 2, 3):
        try:
            i = adapters.index(start + jump)
        except ValueError:
            continue
        if not adapters[i+1:]:
            yield [adapters[i]]
        else:
            for arrangement in get_arrangements_first(adapters[i+1:], adapters[i]):
                yield [start] + arrangement


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else 'input')
