import sys
from copy import deepcopy

class Map():

    def __init__(self,matrix):
        self.mymap = [[c for c in l] for l in matrix]
        self.poi = dict()
        self.shortest_paths = dict()
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] in '0123456789':
                    self.poi[int(matrix[x][y])] = (x,y)

    def __str__(self):
        return '\n'.join([''.join(l) for l in self.mymap]) + '\n' + str(self.poi)

    def get_map_with_path(self,path):
        new_map = deepcopy(self.mymap)
        for (x,y) in path:
            new_map[x][y] = '@'
        return '\n'.join([''.join(l) for l in new_map]) + '\n' + str(self.poi)

    def get_near_points(self,p):
        (x, y) = p
        for (x,y) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if self.mymap[x][y] != '#':
                yield (x,y)

    def find_shortest_path(self,a,b):
        start = self.poi[min(a,b)]
        end = self.poi[max(a,b)]

        #print("searching shortest path from {} {} to {} {}".format(min(a,b),start,min(a,b),end))
        try:
            return self.shortest_paths[(a,b)]
        except KeyError:
            pass

        paths = [(start,[start])]
        seen_points = set([start])
        while True:
            #print(paths)
            (p,path) = paths.pop(0)
            if p == end:
                self.shortest_paths[(a,b)] = path
                return path
            for np in self.get_near_points(p):
                if np not in seen_points:
                    paths.append((np,path+[np]))
                    seen_points.add(np)
            #input()

if __name__ == '__main__':

    if len(sys.argv)>1:
        fname = sys.argv[1]
    else:
        fname = 'input'

    # parse and read map
    m = Map([l.strip() for l in open(fname).readlines()])

    print(m)

    #
    for a in range(10):
        if a not in m.poi:
            break
        for b in range(a+1,10):
            if b not in m.poi:
                break
            m.find_shortest_path(a,b)

    # calculate all the possible paths between points
    paths = list()
    new_paths = [[0]]
    while len(new_paths) > len(paths):
        paths = new_paths
        new_paths = list()
        for p in paths:
            for k in m.poi.keys():
                if k not in p:
                    new_paths.append(p + [k])

    # Step One

    # calculate the shortest path
    min_path = None
    mp = ""
    for p in new_paths:
        total_path = list()
        for c in range(len(p)):
            a = p[c]
            try:
                b = p[c+1]
                total_path = total_path[:-1] + m.find_shortest_path(a,b)
            except IndexError:
                pass

        if min_path:
            if len(min_path) > len(total_path):
                min_path = total_path
                mp = p
        else:
            min_path = total_path
            mp = p

    print(m.get_map_with_path(min_path))

    print("shortest path length: {} ({})".format(len(min_path)-1,''.join([str(c) for c in mp])))
