

if __name__ == '__main__':
    import sys, re

    if len(sys.argv)>1:
        fn = sys.argv[1]
    else:
        fn = 'input'

    discs = [(1,0,0)] # first fake disk, passes always

    with open(fn,'r') as f:
        discs += [[int(d) for d in re.search('Disc #[\d]+ has ([\d]+) positions; at time=([\d]+), it is at position ([\d]+).',l).groups()] for l in f]

    # bruteforce
    time = 0
    passes = False
    while not passes:
        passes = True
        for i in range(len(discs)):
            (num_pos, d_time, pos_time) = discs[i]
            if ((pos_time - d_time + i + time) % num_pos) != 0:
                passes = False
                break
        time += 1
    print(time-1)
