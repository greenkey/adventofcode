import re

floor_names = ['ground','first','second','third','fourth']

floors = [[]]*len(floor_names)
with open('input','r') as f:
    for l in f:
        x = re.search('The ([\w]+) floor contains (.+)\.',l)
        if x:
            floor = floor_names.index(x.group(1))
            if 'nothing' not in l:
                floors[floor] = [''.join([w[0] for w in i.split()]).upper() for i in x.group(2).replace('a ','').replace('-compatible','').split(' and ')]
