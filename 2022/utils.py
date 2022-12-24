import curses
from time import sleep
from typing import Any, Iterable, NamedTuple


class Point2D(NamedTuple):
    x: int
    y: int

    def __add__(s, o):
        o = Point2D(*o)
        return Point2D(s.x + o.x, s.y + o.y)


color_map = {
    "black": 0,
    "red": 1,
    "green": 2,
    "yellow": 3,
    "blue": 4,
    "magenta": 5,
    "cyan": 6,
    "white": 7,
}


def print_map(
    screen,
    points: dict[Point2D, str],
    top_notes="",
    bottom_notes="",
    center=None,
    then_wait=False,
    colors=None,
):
    colors = colors or {}
    char_pair = {}
    for i, (char, color) in enumerate(colors.items(), start=1):
        if "," in color:
            fg, bg = [color_map[c.strip().lower()] for c in color.split(",")]
        else:
            fg = color_map[color.strip().lower()]
            bg = 0
        curses.init_pair(i, fg, bg)  # cyan
        char_pair[char] = i

    maxy, maxx = screen.getmaxyx()
    if center:
        delta_x = maxx // 2 - center.x
        delta_y = maxy // 2 - center.y
    else:
        delta_x = delta_y = 1
    # screen.erase()
    screen.idcok(False)
    screen.idlok(False)

    for x in range(1, maxx - 1):
        for y in range(1, maxy - 1):
            c = points.get((x - delta_x, y - delta_y), " ")
            screen.addstr(y + 1, x, c, curses.color_pair(char_pair.get(c, 0)))

    screen.addstr(0, 0, top_notes)
    screen.addstr(maxy - 1, 0, bottom_notes)
    screen.refresh()
    if then_wait:
        screen.getch()
    else:
        sleep(0.1)
        pass
