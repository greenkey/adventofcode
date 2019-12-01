#!/usr/bin/env python

import fileinput


class MassFuelTableDict(dict):
    def __missing__(self, mas: int) -> int:
        fuel = self[mas] = self._get_fuel_need(mas)
        return fuel

    def _get_fuel_need(self, mass: int) -> int:
        fuel = mass//3-2
        if fuel <= 0:
            fuel = 0
        else:
            fuel += self[fuel]
        return fuel


def test_get_fuel_need():
    t = MassFuelTableDict()
    assert t[12] == 2
    assert t[14] == 2
    assert t[1969] == 966
    assert t[100756] == 50346


if __name__ == '__main__':
    total = 0
    t = MassFuelTableDict()
    for line in fileinput.input():
        total += t[int(line)]
    print(total)
