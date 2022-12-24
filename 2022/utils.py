import curses
from time import sleep
from typing import Any, Iterable, NamedTuple


class Point2D(NamedTuple):
    x: int
    y: int

    def __add__(s, o):
        o = Point2D(*o)
        return Point2D(s.x + o.x, s.y + o.y)


def print_map(
    points: dict[Point2D, str],
    top_notes="",
    bottom_notes="",
    center=None,
    then_wait=False,
):
    def _print(screen):
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
                screen.addstr(y + 1, x, c)

        screen.addstr(0, 0, top_notes)
        screen.addstr(maxy - 1, 0, bottom_notes)
        screen.refresh()
        if then_wait:
            screen.getch()
        else:
            sleep(0.05)

    curses.wrapper(_print)
