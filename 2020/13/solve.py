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

    shifts = [(int(line), i) for i, line in enumerate(bus_lines) if line != 'x']
    freq2, shift2 = shifts.pop(0)
    freq1, shift1 = shifts.pop(0)
    ts = 1
    while True:
        if (ts + shift2) % freq2 == 0:
            if (ts + shift1) % freq1 == 0:
                freq2, shift2 = (freq1 * freq2, freq1 * freq2 - ts)
                try:
                    freq1, shift1 = shifts.pop(0)
                except IndexError:
                    break
                continue
            ts += freq2
        else:
            ts += 1

    print(freq2 - shift2)


if __name__ == "__main__":
    solve(sys.argv[1] if len(sys.argv) > 1 else "input")
