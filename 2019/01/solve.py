import sys
from typing import Union

file_name = sys.argv[1:] or 'input'

def calc_fuel(line: Union[str, int]) -> int:
    return int(line) // 3 - 2

def calc_additional_fuel(fuel: int) -> int:
    additional_fuel = calc_fuel(fuel)
    if additional_fuel > 0:
        return additional_fuel + calc_additional_fuel(additional_fuel)
    else:
        return 0

total_fuel = 0
total_additional_fuel = 0
for line in open(file_name).readlines():
    fuel = calc_fuel(line)
    total_fuel += fuel
    total_additional_fuel += fuel + calc_additional_fuel(fuel)

print(total_fuel)
print(total_additional_fuel)
