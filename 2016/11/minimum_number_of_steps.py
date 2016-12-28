import re

class IsolatedArea():
    floor_names = ['ground','first','second','third','fourth']
    UP = 1
    DOWN = -1

    def __init__(self):
        self.floors = [set()]*len(self.floor_names)
        self.objects = set()
        self.elevator = 1

    def __hash__(self):
        #return hash('\n'.join(['|'.join(sorted(f)) for f in self.floors]))
        return hash(str(self))
        ret = 0
        objects = sorted(self.objects)
        for o in range(len(objects)):
            for f in range(len(self.floors)):
                if objects[o] in self.floors[f]:
                    ret += 4**o*f
        return ret

    def __str__(self):
        return self.pretty_print()

    def __copy__(self):
        new = type(self)()
        new.floors = [set(f) for f in self.floors]
        new.objects = set(self.objects)
        new.elevator = self.elevator
        return new
    def copy(self):
        return self.__copy__()

    def __eq__(self,other):
        return hash(self) == hash(other)

    def read_file(self,filename):
        for l in open(filename):
            x = re.search('The ([\w]+) floor contains (.+)\.',l)
            if x:
                floor = self.floor_names.index(x.group(1))
                if 'nothing' not in l:
                    self.floors[floor] = set([s.strip().split()[0]+s.strip().split()[1][0].upper() for s in x.group(2).replace('-compatible','').replace(',','').replace('and','').split('a ') if s])
                    self.objects.update(self.floors[floor])

    def pretty_print(self):
        ret = ''
        for i in range(len(self.floors)-1,0,-1):
            ret += f'F{i} ' + ('E ' if self.elevator == i else '. ')
            ret += ' '.join([o if o in self.floors[i] else '.'*len(o) for o in sorted(self.objects)]) + '\n'
        return ret

    def is_safe_condition(self):
        # if a chip is ever left in the same area as another RTG, and it's not connected to its own RTG, the chip will be fried
        for objects_on_floor in self.floors:
            for chip in [obj for obj in objects_on_floor if obj[-1]=='M']:
                has_generator = chip[:-1]+'G' in objects_on_floor
                other_generators = len([obj for obj in objects_on_floor if obj[-1]=='G' and not obj.startswith(chip[:-1])])
                if not has_generator and other_generators>0:
                    return False
        return True

    def move(self,objs,direction):
        if len(objs) < 1:
            raise Exception('As a security measure, the elevator will only function if it contains at least one RTG or microchip.')
        if not (1 <= self.elevator+direction <= len(self.floors)):
            raise Exception('Cannot move there')
        f = self.floors[self.elevator]
        for obj in objs:
            if obj not in f:
                raise Exception('Object not present at floor')
        f -= set(objs)
        self.elevator += direction
        self.floors[self.elevator] |= set(objs)

    def next_possible_moves(self):
        current_floor = self.floors[self.elevator]
        for move_direction in [self.UP, self.DOWN]:
            for obj1 in current_floor:
                new = self.copy()
                try:
                    new.move([obj1],move_direction)
                    if new.is_safe_condition():
                        yield new
                except:
                    pass

                for obj2 in current_floor:
                    if obj1 != obj2:
                        new = self.copy()
                        try:
                            new.move([obj1,obj2],move_direction)
                            if new.is_safe_condition():
                                yield new
                        except:
                            pass




if __name__ == '__main__':
    import sys
    if len(sys.argv)>1:
        fname = sys.argv[1]
    else:
        fname = 'input'

    ia = IsolatedArea()
    ia.read_file(fname)

    print(ia)

    next_moves = [[ia]]
    explored_layouts = set()
    while next_moves:
        moves = next_moves.pop(0)
        ia = moves[-1]
        #print(len(explored_layouts),len(next_moves)," ",end='\r')
        if len(ia.floors[4] ^ ia.objects)  == 0:
            print('\n\nfound\n\n')
            break
        for nm in ia.next_possible_moves():
            if nm not in explored_layouts:
                next_moves.append(moves+[nm])
                explored_layouts.add(nm)

    print(f"Moves: {len(moves)-1}")
    for m in moves:
        print(m)
        input()
    print(f"Moves: {len(moves)-1}")
