import sys

def md5(s):
	from hashlib import md5 as sys_md5
	return sys_md5(s.encode()).hexdigest()

def get_open_doors(path,passcode):
    return [True if c in 'bcdef' else False for c in md5(passcode+path)[:4]]

def get_next_paths(path_pos,passcode):
    (path, pos) = path_pos
    (x, y) = pos
    doors = get_open_doors(path,passcode) #udlr
    if doors[0] and y>0:
        yield (path+'U', (x,y-1))
    if doors[1] and y<3:
        yield (path+'D', (x,y+1))
    if doors[2] and x>0:
        yield (path+'L', (x-1,y))
    if doors[3] and x<3:
        yield (path+'R', (x+1,y))


passcode = sys.argv[1]
vault_coord = (3,3)
init_coord = (0,0)
paths = [ ("",init_coord) ]

while paths:
    p = paths.pop()
    if p[1] == vault_coord:
        break
    paths = list(get_next_paths(p,passcode)) + paths

print("Shortest path: {} ({} steps)".format(p[0], len(p[0])))
