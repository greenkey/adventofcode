import re

import solve

answer_example_a = 26
answer_example_b = None

SENSOR = "S"
BEACON = "B"
FIELD = "#"


def manhattan_distance(from_p, to_p):
    dist = 0
    for d in range(100):
        try:
            dist += abs(from_p[d] - to_p[d])
        except IndexError:
            break
    return dist


def manhattan_points(origin, distance, only_y=None):
    ox, oy = origin
    if only_y is None:
        range_y = range(oy - distance, oy + distance + 1)
    else:
        range_y = [only_y]
    for y in range_y:
        distance_x = distance - abs(oy - y)
        for x in range(ox - distance_x, ox + distance_x + 1):
            yield x, y


class SensorMap:
    parse_mask = re.compile(
        r"Sensor at x=([0-9-]+), y=([0-9-]+): closest beacon is at x=([0-9-]+), y=([0-9-]+)"
    )

    def __init__(self, check_y):
        self.map = {}
        self.check_y = check_y
        self.min_x = None
        self.min_y = None
        self.max_x = None
        self.max_y = None

    def parse_data(self, data, print_map=None):
        for line in data.splitlines():
            result = self.parse_mask.findall(line)
            sx, sy, bx, by = map(int, result[0])
            s = (sx, sy)
            b = (bx, by)
            self._set_point(s, SENSOR)
            self._set_point(b, BEACON)
            distance = manhattan_distance(s, b)
            self._draw_sensor_field(s, distance)
            if print_map:
                self.print_map(**print_map)
                input()

    def _set_point(self, p, value):
        self.map[p] = value
        self.min_x = min(p[0] if self.min_x is None else self.min_x, p[0])
        self.min_y = min(p[1] if self.min_y is None else self.min_y, p[1])
        self.max_x = max(p[0] if self.max_x is None else self.max_x, p[0])
        self.max_y = max(p[1] if self.max_y is None else self.max_y, p[1])

    def _draw_sensor_field(self, sensor, distance):
        for p in manhattan_points(sensor, distance, only_y=self.check_y):
            if not self.map.get(p):
                self._set_point(p, FIELD)

    def get_y(self, y):
        for (_, my), val in self.map.items():
            if my == y:
                yield val


def solve_a(data):
    if len(data) == 737:
        check_y = 10
    else:
        check_y = 2000000
    m = SensorMap(check_y=check_y)
    m.parse_data(data)
    return sum(1 for p in m.get_y(check_y) if p == FIELD)


def solve_b(data, example=False):
    return None


if __name__ == "__main__":
    solve.main(2022, 15)
