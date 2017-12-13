import fileinput


def caught_in_firewall(firewall, delay):
    for d, r in firewall.items():
        if (d+delay)%(r*2-2)==0:
            return True
    return False


if __name__ == '__main__':
    severity = 0
    firewall = dict()
    for line in fileinput.input():
        d, r = [int(x) for x in line.split(': ')]
        firewall[d] = r
        if d%(r*2-2)==0:
            severity += d*r
    print(severity)

    i = 0
    while True:
        i += 1
        if not caught_in_firewall(firewall, i):
            print(i)
            break

