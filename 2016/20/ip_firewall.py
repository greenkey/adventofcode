

blacklist = set()

[blacklist.add(tuple([int(i) for i in l.strip().split('-')])) for l in open('input')]

curmax = 0
found = False
while not found:
	found = True
	i = curmax
	for (start,end) in list(blacklist):
		if start <= i <= end:
			curmax = max(curmax, end+1)
			blacklist.remove((start,end))
			found = False
	if found:
		print(curmax)
		break