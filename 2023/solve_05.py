from typing import Iterable, Sequence
from run import runme

year = 2023
day = 5


class Map:
    def __init__(self) -> None:
        self.map: list[tuple[int, int, int]] = []

    def add_map(self, dst_start: int, src_start: int, length: int):
        self.map.append((src_start, dst_start, length))
        self.map.sort()

    def locate(self, src: int) -> int:
        for src_start, dst_start, length in self.map:
            if src_start <= src < src_start + length:
                return dst_start + src - src_start
        return src
    

class Almanac:
    def __init__(self, seeds) -> None:
        self.seeds: Sequence[int] = seeds
        self.maps: list[Map] = []


def parse_seeds(line: str, ranges=False) -> Sequence[int]:
    if ranges:
        ranges = [int(n) for n in line.split()[1:]]
        for seed_range_start, seed_range_length in zip(ranges[::2], ranges[1::2]):
            yield from range(seed_range_start, seed_range_start + seed_range_length)
    else:
        for n in line.split()[1:]:
            yield int(n)


def parse_data(data, seed_ranges=False) -> Almanac:
    lines = (line for line in data.splitlines())
    first_line = next(lines)
    seeds = parse_seeds(first_line, seed_ranges)
    almanac = Almanac(seeds)
    
    current_map = None
    for line in lines:
        if line == "":
            continue
        parts = line.split()
        if len(parts) == 2:
            current_map = Map()
            almanac.maps.append(current_map)
        if len(parts) == 3:
            dst_start, src_start, length = [int(part) for part in parts]
            current_map.add_map(int(dst_start), int(src_start), int(length))
    
    return almanac


def solve_a(data):
    almanac = parse_data(data)
    
    things = almanac.seeds

    min_n = None

    for n in things:
        for map in almanac.maps:
            n = map.locate(n)
        if min_n is None or n < min_n:
            min_n = n

    return min_n


def solve_b(data):
    almanac = parse_data(data, seed_ranges=True)
    
    things = almanac.seeds

    min_n = None

    for i, n in enumerate(things):
        print(f"min found: {min_n} -- seeds processed: {i}", end="\r")
        for map in almanac.maps:
            n = map.locate(n)
        if min_n is None or n < min_n:
            min_n = n

    return min_n



if __name__ == "__main__":
    runme()
