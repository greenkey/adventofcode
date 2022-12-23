from collections import Counter, deque
from time import sleep

import solve

answer_example_a = 110
answer_example_b = 20

ELF = "\033[0;32m#\033[0m"
EMPTY = "\033[0;34m.\033[0m"
MOVE = "\033[0;33mo\033[0m"


class ElvesMap:
    dir = {
        "N": ((-1, -1), (0, -1), (1, -1)),
        "S": ((-1, 1), (0, 1), (1, 1)),
        "W": ((-1, -1), (-1, 0), (-1, 1)),
        "E": ((1, -1), (1, 0), (1, 1)),
    }

    def __init__(self, data: str):
        self.elves = set()
        self.dir_order = deque("NSWE")
        for y, line in enumerate(data.splitlines()):
            for x, val in enumerate(line):
                if val == "#":
                    self.elves.add((x, y))
        self.rounds = 0

    def get_boundaries(self, additional=None):
        coords = self.elves.copy()
        if additional:
            coords.update(additional)
        xs, ys = zip(*coords)
        return (min(xs), min(ys)), (max(xs), max(ys))

    def print(self, animation=None, moves=None):
        if not animation:
            return

        print(chr(27) + "[2J")  # clear screen

        (minx, miny), (maxx, maxy) = self.get_boundaries(additional=moves)
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                char = EMPTY
                if (x, y) in self.elves:
                    char = ELF
                if moves and (x, y) in moves:
                    char = MOVE
                print(char, end="")
            print()
        area = (abs(maxy - miny) + 1) * (abs(maxx - minx) + 1)
        print(
            f"round={self.rounds}, elves={len(self.elves)}, {area=}, empty={area-len(self.elves)}"
        )

        if animation > 1:
            input()
        else:
            sleep(animation)

    def move_for_elf(self, elf):
        ex, ey = elf
        possible_moves = []
        for dir in self.dir_order:
            for dx, dy in self.dir[dir]:
                if (ex + dx, ey + dy) in self.elves:
                    break
            else:
                dx, dy = self.dir[dir][1]
                possible_moves.append((ex + dx, ey + dy))
        if 0 < len(possible_moves) < 4:
            return possible_moves[0]

    def propose_moves(self) -> dict:
        next_positions = dict()
        for elf in self.elves:
            if move := self.move_for_elf(elf):
                if not move or move == elf:
                    continue
                if move in next_positions:
                    next_positions[move] = None
                else:
                    next_positions[move] = elf
        return dict((k, v) for k, v in next_positions.items() if v)

    def move(self, moves: dict):
        if not moves:
            return False

        newpos, oldpos = zip(*moves.items())
        self.elves.difference_update(oldpos)
        self.elves.update(newpos)
        return True

    def run(self, n=None, animation=False):
        if n:
            check = lambda: self.rounds < n
        else:
            check = lambda: True

        while check():
            self.rounds += 1
            print(f"round={self.rounds}", end="\r")
            moves = self.propose_moves()

            # self.print(animation, moves=moves.keys())

            if not self.move(moves):
                break

            self.print(animation)

            self.dir_order.rotate(-1)
        return self.rounds


def test_move_for_elf():
    elves = ElvesMap("\n".join(["...", ".#.", "..."]))
    assert elves.move_for_elf((1, 1)) == None

    elves = ElvesMap("\n".join(["#..", ".#.", "..."]))
    assert elves.move_for_elf((1, 1)) == (1, 2)

    elves = ElvesMap("\n".join([".#.", ".#.", "..."]))
    assert elves.move_for_elf((1, 1)) == (1, 2)

    elves = ElvesMap("\n".join(["..#", ".#.", "..."]))
    assert elves.move_for_elf((1, 1)) == (1, 2)

    elves = ElvesMap("\n".join(["...", "##.", "..."]))
    assert elves.move_for_elf((1, 1)) == (1, 0)

    elves = ElvesMap("\n".join(["...", ".##", "..."]))
    assert elves.move_for_elf((1, 1)) == (1, 0)

    elves = ElvesMap("\n".join(["...", ".#.", "#.."]))
    assert elves.move_for_elf((1, 1)) == (1, 0)

    elves = ElvesMap("\n".join(["...", ".#.", ".#."]))
    assert elves.move_for_elf((1, 1)) == (1, 0)

    elves = ElvesMap("\n".join(["...", ".#.", "..#"]))
    assert elves.move_for_elf((1, 1)) == (1, 0)

    elves = ElvesMap("\n".join(["#..", ".#.", "..#"]))
    assert elves.move_for_elf((1, 1)) == None

    elves = ElvesMap("\n".join(["#.#", ".#.", "..."]))
    assert elves.move_for_elf((1, 1)) == (1, 2)

    elves = ElvesMap("\n".join(["#..", ".#.", "#.."]))
    assert elves.move_for_elf((1, 1)) == (2, 1)

    elves = ElvesMap("\n".join(["..#", ".#.", "..#"]))
    assert elves.move_for_elf((1, 1)) == (0, 1)


def test_propose_moves():
    elves = ElvesMap("\n".join(["...", ".#.", "..."]))
    assert elves.propose_moves() == {}

    elves = ElvesMap("\n".join(["#..", ".#.", "..."]))
    assert elves.propose_moves() == {
        (0, -1): (0, 0),
        (1, 2): (1, 1),
    }

    elves = ElvesMap("\n".join([".#.", ".#.", "..."]))
    assert elves.propose_moves() == {
        (1, -1): (1, 0),
        (1, 2): (1, 1),
    }

    elves = ElvesMap("\n".join(["..#", ".#.", "..."]))
    assert elves.propose_moves() == {
        (2, -1): (2, 0),
        (1, 2): (1, 1),
    }

    elves = ElvesMap("\n".join(["...", "##.", "..."]))
    assert elves.propose_moves() == {
        (0, 0): (0, 1),
        (1, 0): (1, 1),
    }

    elves = ElvesMap("\n".join(["...", ".##", "..."]))
    assert elves.propose_moves() == {
        (2, 0): (2, 1),
        (1, 0): (1, 1),
    }

    elves = ElvesMap("\n".join(["...", ".#.", "#.."]))
    assert elves.propose_moves() == {
        (1, 0): (1, 1),
        (0, 3): (0, 2),
    }

    elves = ElvesMap("\n".join(["...", ".#.", ".#."]))
    assert elves.propose_moves() == {
        (1, 0): (1, 1),
        (1, 3): (1, 2),
    }

    elves = ElvesMap("\n".join(["...", ".#.", "..#"]))
    assert elves.propose_moves() == {
        (1, 0): (1, 1),
        (2, 3): (2, 2),
    }

    elves = ElvesMap("\n".join(["#..", ".#.", "..#"]))
    assert elves.propose_moves() == {
        (0, -1): (0, 0),
        (2, 3): (2, 2),
    }

    elves = ElvesMap("\n".join(["#.#", ".#.", "..."]))
    assert elves.propose_moves() == {
        (0, -1): (0, 0),
        (2, -1): (2, 0),
        (1, 2): (1, 1),
    }

    elves = ElvesMap("\n".join(["#..", ".#.", "#.."]))
    assert elves.propose_moves() == {
        (0, -1): (0, 0),
        (2, 1): (1, 1),
        (0, 3): (0, 2),
    }

    elves = ElvesMap("\n".join(["..#", ".#.", "..#"]))
    assert elves.propose_moves() == {
        (2, -1): (2, 0),
        (0, 1): (1, 1),
        (2, 3): (2, 2),
    }

    elves = ElvesMap("##")
    assert elves.propose_moves() == {
        (0, -1): (0, 0),
        (1, -1): (1, 0),
    }

    elves = ElvesMap("\n".join(["###", "###", "###"]))
    assert elves.propose_moves() == {
        (0, -1): (0, 0),
        (1, -1): (1, 0),
        (2, -1): (2, 0),
        (-1, 1): (0, 1),
        (3, 1): (2, 1),
        (0, 3): (0, 2),
        (1, 3): (1, 2),
        (2, 3): (2, 2),
    }


def solve_a(data: str):
    elves = ElvesMap(data)
    elves.run(n=10, animation=None)

    (minx, miny), (maxx, maxy) = elves.get_boundaries()
    places = (abs(maxx - minx) + 1) * (abs(maxy - miny) + 1)
    empty = places - len(elves.elves)
    return empty


def test_b():
    data = "\n".join(
        [
            ".....",
            "..##.",
            "..#..",
            ".....",
            "..##.",
            ".....",
        ]
    )
    assert solve_b(data) == 4

    assert solve_b("#") == 1

    assert solve_b("##") == 4


def solve_b(data):
    elves = ElvesMap(data)
    last_round = elves.run(animation=None)
    return last_round


if __name__ == "__main__":
    solve.main(2022, 23)
