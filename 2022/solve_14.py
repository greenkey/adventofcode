from collections import defaultdict
from time import sleep

import solve

answer_example_a = 24
answer_example_b = 93


AIR = "\033[0;34m.\033[0m"
ROCK = "\033[0;31m#\033[0m"
SAND = "\033[0;33mo\033[0m"
SAND_TRACE = "\033[0;36m~\033[0m"


class InfiniteFlow(Exception):
    pass


def get_points(p_from, p_to):
    fx, fy = p_from
    tx, ty = p_to
    dir_x = -1 if tx < fx else +1
    dir_y = -1 if ty < fy else +1
    for x in range(fx, tx + dir_x, dir_x):
        for y in range(fy, ty + dir_y, dir_y):
            yield x, y


class CaveSlice:
    def __init__(self, rock_data, with_ground=False) -> None:
        self.sand_source = (500, 0)
        self.with_ground = with_ground
        self.map = defaultdict(int)
        self.min_x = 500
        self.max_x = 500
        self.max_y = 0
        self.min_y = 0
        self._parse_data(rock_data)

    def _parse_data(self, rock_data):
        for rock_line in rock_data.splitlines():
            segments = [[int(c) for c in s.split(",")] for s in rock_line.split(" -> ")]
            for i in range(len(segments) - 1):
                for x, y in get_points(*segments[i : i + 2]):
                    self._set_point(x, y, ROCK)
        if self.with_ground:
            y = self.max_y + 2
            for x in range(self.min_x - y - 2, self.max_x + 1 + y + 2):
                self._set_point(x, y, ROCK)

    def _set_point(self, x, y, value):
        self.map[x, y] = ROCK
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def print(self):
        print("\033c", end="")
        toprint = []
        for y in range(self.min_y, self.max_y + 1):
            line = []
            for x in range(self.min_x, self.max_x + 1):
                line.append(self.map.get((x, y), AIR))
            toprint.append("".join(line))
        print("\n".join(toprint))

    def drop_sand(self):
        ignore = (SAND_TRACE, AIR, None)
        x, y = self.sand_source
        while True:
            self.map[x, y] = SAND_TRACE
            if x > self.max_x or x < self.min_x or y > self.max_y:
                raise InfiniteFlow()
            elif self.map.get((x, y + 1)) in ignore:
                y += 1
            elif self.map.get((x - 1, y + 1)) in ignore:
                y += 1
                x -= 1
            elif self.map.get((x + 1, y + 1)) in ignore:
                y += 1
                x += 1
            elif (x, y) == self.sand_source:
                self.map[x, y] = SAND
                raise InfiniteFlow()
            else:
                break
        self.map[x, y] = SAND


def solve_a(data):
    m = CaveSlice(data)
    while True:
        try:
            m.drop_sand()
        except InfiniteFlow:
            break
        finally:
            sleep(0.05)
            m.print()
            pass
    m.print()
    input()
    return sum([1 for v in m.map.values() if v == SAND])


def solve_b(data):
    m = CaveSlice(data, with_ground=True)
    while True:
        try:
            m.drop_sand()
        except InfiniteFlow:
            break
        finally:
            sleep(0.05)
            m.print()
            pass
    m.print()
    return sum([1 for v in m.map.values() if v == SAND])


if __name__ == "__main__":
    solve.main(2022, 14)
