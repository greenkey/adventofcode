from collections import defaultdict
from typing import Dict, List


def count_orbits(
    orbit_map: Dict[str, List[str]], start: str = "COM", depth: int = 1
) -> int:
    count = 0
    for new_start in orbit_map[start]:
        count += 1 * depth + count_orbits(orbit_map, new_start, depth + 1)
    return count


def transfers(reverse_map: Dict[str, List[str]], a: str, b: str) -> int:
    path_a: List[str] = []
    path_b: List[str] = []
    while True:
        a = reverse_map.get(a)
        if a in path_b:
            return len(path_a) + path_b.index(a)
        path_a.append(a)

        b = reverse_map.get(b)
        if b in path_a:
            return len(path_b) + path_a.index(b)
        path_b.append(b)


def solve(file_name: str = "input"):
    orbit_map = defaultdict(list)
    for relationship in open(file_name).readlines():
        center_object, satellite = relationship.strip().split(")")
        orbit_map[center_object].append(satellite)

    print(count_orbits(orbit_map))

    reverse_map = {sat: grav for grav, sats in orbit_map.items() for sat in sats}
    print(transfers(reverse_map, "YOU", "SAN"))


if __name__ == "__main__":
    solve()
