from itertools import count

import solve

answer_example_a = 21
answer_example_b = None

BLUE = "\033[94m"
GREEN = "\033[92m"
ENDC = "\033[0m"
DEBUG = False


def print_trees(trees, visibles, X, Y, cx, cy):
    if not DEBUG:
        return
    print("-" * Y)
    for y in range(Y + 1):
        for x in range(X + 1):
            tree = trees[(x, y)]
            if (x, y) == (cx, cy):
                tree = f"{BLUE}{tree}{ENDC}"
            if (x, y) in visibles:
                tree = f"{GREEN}{tree}{ENDC}"
            print(tree, end="")
        print()
    input()


def solve_a(data):
    visible_trees = set()  # a set of x,y to save all the visible trees
    X = Y = 0

    # save map
    trees = dict()
    for y, line in enumerate(data.splitlines()):
        for x, item in enumerate(line):
            trees[(x, y)] = int(item)
            X = max(X, x)
            Y = max(Y, y)

    # horizontal
    for y in range(Y + 1):
        max_height = -1
        for x in range(X + 1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height
            print_trees(trees, visible_trees, X, Y, x, y)
        max_height = -1
        for x in range(X, -1, -1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height
            print_trees(trees, visible_trees, X, Y, x, y)

    # vertical
    for x in range(X + 1):
        max_height = -1
        for y in range(Y + 1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height
            print_trees(trees, visible_trees, X, Y, x, y)
        max_height = -1
        for y in range(Y, -1, -1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height
            print_trees(trees, visible_trees, X, Y, x, y)

    return len(visible_trees)


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 8)
