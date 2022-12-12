import solve

answer_example_a = 31
answer_example_b = 29


directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


class MyMap:
    def __init__(self, data):
        self.mymap = dict()
        self.origin = (-1, -1)
        self.goal = (-1, -1)
        for y, line in enumerate(data.splitlines()):
            for x, c in enumerate(line):
                if c == "S":
                    self.origin = (x, y)
                    self.mymap[x, y] = ord("a")
                elif c == "E":
                    self.goal = (x, y)
                    self.mymap[x, y] = ord("z")
                else:
                    self.mymap[x, y] = ord(c)

    def next_step(self, from_x, from_y, reverse=False):
        cur = self.mymap[from_x, from_y]

        for dx, dy in directions:
            x = from_x + dx
            y = from_y + dy
            if next_p := self.mymap.get((x, y)):
                if reverse and next_p >= cur - 1:
                    yield x, y
                elif not reverse and next_p <= cur + 1:
                    yield x, y


def solve_a(data):
    mymap = MyMap(data)
    visited = set()
    current_positions = set([mymap.origin])

    length = 0
    while mymap.goal not in current_positions:
        next_positions = set()
        for p in current_positions:
            next_positions.update(mymap.next_step(*p))
        current_positions = next_positions - visited
        visited.update(next_positions)
        length += 1
        print(f"{len(visited)=}", end="\r")

    return length


def solve_b(data):
    mymap = MyMap(data)
    visited = set()
    current_positions = set([mymap.goal])
    height = mymap.mymap[mymap.goal]

    length = 0
    while height > ord("a"):
        next_positions = set()
        for p in current_positions:
            next_positions.update(mymap.next_step(*p, reverse=True))
        current_positions = next_positions - visited
        visited.update(next_positions)
        length += 1
        height = min(mymap.mymap[p] for p in next_positions)
        print(f"{len(visited)=}", end="\r")

    return length


if __name__ == "__main__":
    solve.main(2022, 12)
