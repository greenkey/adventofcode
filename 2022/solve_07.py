from collections import defaultdict

import solve

answer_example_a = 95437
answer_example_b = None
example_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class FS:
    def __init__(self):
        self.root = {"*meta": {"type": "d"}}
        self.cwd = self.root

    def cd(self, dir):
        match dir:
            case "/":
                self.cwd = self.root
            case _:
                if dir not in self.cwd:
                    self.cwd[dir] = {"..": self.cwd, "*meta": {"type": "d"}}
                self.cwd = self.cwd[dir]

    def touch(self, name, size):
        self.cwd[name] = {"*meta": {"size": int(size), "type": "f"}}

    def du(self, dir=None):
        dir = dir or self.root
        cur_size = 0
        for name, item in dir.items():
            if name.startswith("*"):
                continue
            if name == "..":
                continue
            match (meta := item["*meta"])["type"]:
                case "d":
                    for size in self.du(dir=item):
                        yield size
                        cur_size += size
                case "f":
                    cur_size += meta["size"]
        yield cur_size


def solve_a(data):
    fs = FS()
    for line in data.splitlines():
        match line.split():
            case "$", "cd", dir:
                fs.cd(dir)
            case "$", "ls":
                pass
            case "dir", dir:
                pass
            case size, name:
                fs.touch(name, int(size))

    total_size = 0
    for size in fs.du():
        if size <= 100000:
            total_size += size

    return total_size


def solve_b(data):
    return None


if __name__ == "__main__":
    solve.main(2022, 7)
