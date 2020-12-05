file_name = 'input'

def calculate_seat_id(ticket):
    return int(ticket.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

with open(file_name, 'r') as f:
    tickets = f.readlines()

ticket_ids = set(calculate_seat_id(ticket) for ticket in tickets)

print(max(ticket_ids))

for ticket_id in ticket_ids:
    if ticket_id + 2 in ticket_ids and ticket_id + 1 not in ticket_ids:
        print(ticket_id + 1)
        break
    elif ticket_id - 2 in ticket_ids and ticket_id - 1 not in ticket_ids:
        print(ticket_id - 1)
        break
