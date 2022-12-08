from itertools import count

import solve

answer_example_a = 21
answer_example_b = 8


def get_tree_map(data):
    X = Y = 0

    # save map
    trees = dict()
    for y, line in enumerate(data.splitlines()):
        for x, item in enumerate(line):
            trees[(x, y)] = int(item)
            X = max(X, x)
            Y = max(Y, y)

    return trees, X, Y


def get_visible(trees, startX, startY, endX, endY, height=None):
    highest = -1
    if startX == endX:
        x = startX
        dirY = +1 if endY >= startY else -1
        for y in range(startY + dirY, endY + dirY, dirY):
            th = trees[x, y]
            if th > highest:
                highest = th - 1
                yield x, y
            if th >= height:
                break
        else:
            yield x, y
    elif startY == endY:
        y = startY
        dirX = +1 if endX >= startX else -1
        for x in range(startX + dirX, endX + dirX, dirX):
            th = trees[x, y]
            if th > highest:
                highest = th - 1
                yield x, y
            if th >= height:
                break
        else:
            yield x, y


def solve_a(data):
    visible_trees = set()  # a set of x,y to save all the visible trees
    trees, X, Y = get_tree_map(data)

    # horizontal
    for y in range(Y + 1):
        # left to right
        max_height = -1
        for x in range(X + 1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height
        # right to left
        max_height = -1
        for x in range(X, -1, -1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height

    # vertical
    for x in range(X + 1):
        # top down
        max_height = -1
        for y in range(Y + 1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height
        # bottom up
        max_height = -1
        for y in range(Y, -1, -1):
            if (height := trees[(x, y)]) > max_height:
                visible_trees.add((x, y))
                max_height = height

    return len(visible_trees)


def solve_b(data):
    max_score = 0
    trees, X, Y = get_tree_map(data)

    for tx in range(1, X):
        for ty in range(1, Y):
            score = 1
            height = trees[tx, ty]

            farer = list(get_visible(trees, tx, ty, tx, 0, height=height))
            fx, fy = farer[-1]
            m = abs(tx - fx) + abs(ty - fy)
            score *= m

            farer = list(get_visible(trees, tx, ty, tx, Y, height=height))
            fx, fy = farer[-1]
            m = abs(tx - fx) + abs(ty - fy)
            score *= m

            farer = list(get_visible(trees, tx, ty, 0, ty, height=height))
            fx, fy = farer[-1]
            m = abs(tx - fx) + abs(ty - fy)
            score *= m

            farer = list(get_visible(trees, tx, ty, X, ty, height=height))
            fx, fy = farer[-1]
            m = abs(tx - fx) + abs(ty - fy)
            score *= m

            max_score = max(max_score, score)
    return max_score


if __name__ == "__main__":
    solve.main(2022, 8)
