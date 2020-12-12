from collections import defaultdict
from typing import Dict, List


def count_orbits(
    orbit_map: Dict[str, List[str]], start: str = "COM", depth: int = 1
) -> int:
    count = 0
    for new_start in orbit_map[start]:
        count += 1 * depth + count_orbits(orbit_map, new_start, depth + 1)
    return count


def solve(file_name: str = "input"):
    orbit_map = defaultdict(list)
    for relationship in open(file_name).readlines():
        center_object, satellite = relationship.strip().split(")")
        orbit_map[center_object].append(satellite)

    print(count_orbits(orbit_map))


if __name__ == "__main__":
    solve()
