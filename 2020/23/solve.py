import sys


def iter_linked_list(ll, start, count=None):
    count = count or len(ll)
    for _ in range(count):
        yield start
        start = ll[start]


def crab_game(cups, times, current_cup):
    greatest = max(cups.keys())
    for i in range(times):
        pick_up1 = cups[current_cup]
        pick_up2 = cups[pick_up1]
        pick_up3 = cups[pick_up2]
        pick_up = [pick_up1, pick_up2, pick_up3]

        destination = current_cup
        while True:
            destination -= 1
            if destination <= 0:
                destination = greatest
            if destination in pick_up:
                continue
            break
        cups[current_cup] = cups[pick_up3]
        current_cup = cups[pick_up3]
        cups[pick_up3] = cups[destination]
        cups[destination] = pick_up1

    return cups


def solve(file_name: str):
    cups_string = open(file_name).read().strip()
    cups = {int(cups_string[i]): int(cups_string[i+1]) for i in range(len(cups_string) - 1)}
    cups[int(cups_string[-1])] = int(cups_string[0])

    new_cups = crab_game(cups.copy(), 100, current_cup=int(cups_string[0]))
    i = 1
    ret = []
    while len(ret) < len(new_cups) - 1:
        ret.append(new_cups[i])
        i = new_cups[i]
    print(''.join(str(x) for x in ret))

    next_n = max(cups.keys()) + 1
    cups[int(cups_string[-1])] = next_n
    for i in range(next_n, 1_000_001):
        cups[i] = i + 1
    cups[1_000_000] = int(cups_string[0])
    cups = crab_game(cups, 10_000_000, int(cups_string[0]))
    three_cups = list(iter_linked_list(cups, 1, 3))
    print(three_cups[1] * three_cups[2])


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
