from math import ceil, floor, sqrt

from run import runme

year = 2023
day = 6

answer_example_a = "288"
answer_example_b = "71503"


def solve_a(data):
    times, distances = (
        [int(x) for x in line.split()[1:]] for line in data.splitlines()
    )
    return solve_for_times_and_distances(times, distances)


def solve_b(data):
    times, distances = (
        [int(line.split(":")[1].replace(" ", ""))] for line in data.splitlines()
    )
    return solve_for_times_and_distances(times, distances)


def solve_for_times_and_distances(times, distances):
    total = 1
    for time, distance in zip(times, distances):
        x1, x2 = calc(time, distance)
        diff = ceil(x2) - floor(x1) - 1
        total *= diff
    return total


def calc(time, distance):
    y = time
    z = distance
    # I need to find the values of x for which:
    # x * (y-x) > z
    # x * y - x^2 > z
    # x * y - x^2 - z > 0
    # x^2 - x * y + z < 0
    a = 1
    b = -y
    c = z
    # x1 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    # x2 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return (
        (-b - sqrt(b**2 - 4 * a * c)) / (2 * a),
        (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
    )


if __name__ == "__main__":
    runme()
