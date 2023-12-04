from collections import defaultdict
from run import runme

year = 2023
day = 3


def solve_a(data):
    matrix = _create_matrix(data)
    numbers = list(_get_numbers(matrix))

    nums_close_to_symbol = [
        num
        for num, coords in numbers
        if any(list(_get_close_symbols(coord, matrix)) for coord in coords)
    ]
    return sum(nums_close_to_symbol)


def solve_b(data):
    matrix = _create_matrix(data)
    numbers = list(_get_numbers(matrix))

    gears = defaultdict(list)
    for num, coords in numbers:
        close_symbols = sum(
            (list(_get_close_symbols(coord, matrix)) for coord in coords), start=[]
        )
        close_symbols = set(close_symbols)
        if not close_symbols:
            continue

        for symbol, coord in close_symbols:
            if symbol == "*":
                gears[coord].append(num)

    total = 0
    for coord, nums in gears.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]

    return total


def _create_matrix(data):
    matrix = dict()
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            matrix[(x, y)] = char
    return matrix


def _get_numbers(matrix):
    x = y = 0
    while True:
        try:
            char = matrix[(x, y)]
        except KeyError:
            # out of bounds
            if x == 0:
                # end of matrix
                break
            # next line
            x = 0
            y += 1
            continue

        if char not in "0123456789":
            x += 1
            continue

        # found number, continue until the number is finished
        num_str = char
        coords = [(x, y)]
        while True:
            x += 1
            try:
                char = matrix[(x, y)]
            except KeyError:
                break
            if char not in "0123456789":
                break
            num_str += char
            coords.append((x, y))
        num = int(num_str)
        yield num, coords
        x += 1


def _get_close_symbols(coord, matrix):
    x, y = coord
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            try:
                char = matrix[(x + dx, y + dy)]
            except KeyError:
                continue
            if char not in "0123456789.":
                yield char, (x + dx, y + dy)


if __name__ == "__main__":
    runme()
