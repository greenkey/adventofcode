import re
from functools import partial

file_name = 'input'

def calculate_seat_id(ticket):
    row = int(ticket[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(ticket[-3:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + column

with open(file_name, 'r') as f:
    tickets = f.readlines()

print(max(calculate_seat_id(ticket) for ticket in tickets))