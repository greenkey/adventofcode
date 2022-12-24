from collections import defaultdict

import solve
from utils import Point2D, print_map

answer_example_a = 18
answer_example_b = 54
example_data = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""


dir_move = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}
moves = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


class BlizzardMap:
    def __init__(self) -> None:
        self.start = (1, 0)
        self.end = (0, 0)
        self.blizzards = defaultdict(list)
        self.walls = dict()
        self.x_size = 0
        self.y_size = 0

    def parse(self, data: str):
        for y, line in enumerate(data.splitlines()):
            for x, val in enumerate(line):
                if val == "." and y == 0:
                    self.start = Point2D(x, y)
                elif val == ".":
                    self.end = Point2D(x, y)
                elif val in dir_move:
                    self.blizzards[Point2D(x, y)].append(val)
                elif val == "#":
                    self.walls[Point2D(x, y)] = "#"
        self.x_size = x
        self.y_size = y

    def get_points(self):
        return {**self.walls, **{p: str(len(b)) for p, b in self.blizzards.items()}}

    def print(self, then_wait=False, top_notes: str = "", additional_points=None):
        points = additional_points or {}
        points.update(self.get_points())
        print_map(points, then_wait=then_wait, top_notes=top_notes)

    def move_blizzards(self):
        new_blizzards = defaultdict(list)
        for pos, dirs in self.blizzards.items():
            for dir in dirs:
                match dir:
                    case ">":
                        x = max((pos.x + 1) % (self.x_size), 1)
                        y = pos.y
                    case "<":
                        if pos.x == 1:
                            x = self.x_size - 1
                        else:
                            x = pos.x - 1
                        y = pos.y
                    case "^":
                        if pos.y == 1:
                            y = self.y_size - 1
                        else:
                            y = pos.y - 1
                        x = pos.x
                    case "v":
                        y = max((pos.y + 1) % (self.y_size), 1)
                        x = pos.x
                new_blizzards[Point2D(x, y)].append(dir)
        self.blizzards = new_blizzards

    def possible_moves(self, pos):
        if self.is_free(pos):
            yield pos
        for move in moves:
            new_pos = pos + move
            if self.is_free(new_pos):
                yield new_pos

    def is_free(self, pos):
        if pos in self.blizzards:
            return False
        if pos in self.walls:
            return False
        return 0 <= pos.x <= self.x_size and 0 <= pos.y <= self.y_size

    def go(self, from_p: Point2D, to_p: Point2D) -> int:
        final_points = {from_p}
        minute = 0
        while True:
            self.move_blizzards()
            minute += 1
            final_points = {p for fp in final_points for p in self.possible_moves(fp)}
            print(f"{minute=}, paths={len(final_points)}", end="\r")
            if to_p in final_points:
                break
        return minute


def solve_a(data):
    m = BlizzardMap()
    m.parse(data)
    return m.go(m.start, m.end)


def solve_b(data):
    m = BlizzardMap()
    m.parse(data)
    return m.go(m.start, m.end) + m.go(m.end, m.start) + m.go(m.start, m.end)


if __name__ == "__main__":
    solve.main(2022, 24)
