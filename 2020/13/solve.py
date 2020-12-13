import math
import sys


def solve(file_name: str):
    my_ts, bus_lines = open(file_name).readlines()
    my_ts = int(my_ts)
    bus_lines = bus_lines.strip().split(",")

    next_ts_buses = {
        math.ceil(my_ts / int(line)) * int(line): line
        for line in bus_lines
        if line != "x"
    }

    next_ts = min(next_ts_buses.keys())
    line = int(next_ts_buses[next_ts])

    print((next_ts - my_ts) * line)


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
