from collections import defaultdict

import solve

answer_example_a = 95437
answer_example_b = 24933642
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
        self.sizes = defaultdict(int)

    def parse(self, data):
        cwd = tuple()
        for line in data.splitlines():
            match line.split():
                case "$", "cd", "..":
                    cwd = cwd[:-1]
                case "$", "cd", dir:
                    cwd = cwd + (dir,)
                case "$", "ls":
                    pass
                case "dir", dir:
                    pass
                case size, _:
                    self.sizes[cwd] += int(size)
        other = self.sizes.copy()
        for dir, size in other.items():
            while dir:
                dir = dir[:-1]
                self.sizes[dir] += size

    def du(self):
        return list(self.sizes.values())


def solve_a(data):
    fs = FS()
    fs.parse(data)

    total_size = 0
    for size in fs.du():
        if size <= 100000:
            total_size += size

    return total_size


def solve_b(data):
    fs = FS()
    fs.parse(data)

    storage_size = 70_000_000
    space_needed = 30_000_000

    sizes = list(fs.du())
    used_space = max(sizes)
    assert storage_size >= used_space

    unused = storage_size - used_space
    to_free = space_needed - unused

    return min(size for size in sizes if size >= to_free)


if __name__ == "__main__":
    solve.main(2022, 7)
