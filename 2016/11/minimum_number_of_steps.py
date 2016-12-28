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
        ret = str(self.elevator)+'+'
        for f in range(len(self.floors)):
            floor = sorted(self.floors[f])
            for obj in floor:
                if obj[:-1]+('M' if obj[-1]=='G' else 'G') in floor:
                    ret += 'couple-'
                else:
                    ret += obj + '-'
            ret += '\n'
        return hash(ret)

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

    def add(self,object_desc,floor):
        object_desc = object_desc.replace('-compatible','')
        object_desc = object_desc.strip().split()[0]+object_desc.strip().split()[1][0].upper()
        self.floors[floor].add(object_desc)
        self.objects.add(object_desc)

    def next_possible_moves(self):
        current_floor = self.floors[self.elevator]
        directions = [self.UP]
        if sum([len(f) for f in self.floors[:self.elevator]]) > 0:
            directions.append(self.DOWN)
        for move_direction in directions:
            for obj1 in current_floor:
                found = False

                # try to move up two objects
                if move_direction == self.UP:
                    for obj2 in current_floor:
                        if obj1 != obj2:
                            new = self.copy()
                            try:
                                new.move([obj1,obj2],move_direction)
                                if new.is_safe_condition():
                                    yield new
                                    found = True
                            except:
                                pass

                # not found any move, either try to go down or move up one object
                if not found:
                    new = self.copy()
                    try:
                        new.move([obj1],move_direction)
                        if new.is_safe_condition():
                            yield new
                    except:
                        pass






if __name__ == '__main__':
    import sys
    #from time import time

    if len(sys.argv)>1:
        fname = sys.argv[1]
    else:
        fname = 'input'

    ia = IsolatedArea()
    ia.read_file(fname)

    print(ia)

    #next_moves = [[ia]]
    #explored_layouts = set()
    #while next_moves:
    #    moves = next_moves.pop(0)
    #    ia = moves[-1]
    #    #print(len(explored_layouts),len(next_moves)," ",end='\r')
    #    if len(ia.floors[4] ^ ia.objects)  == 0:
    #        print('\n\nfound\n\n')
    #        break
    #    for nm in ia.next_possible_moves():
    #        if nm not in explored_layouts:
    #            next_moves.append(moves+[nm])
    #            explored_layouts.add(nm)

    #print(f"Moves: {len(moves)-1}")

    ia.add('elerium generator',1)
    ia.add('elerium-compatible microchip',1)
    ia.add('dilithium generator',1)
    ia.add('dilithium-compatible microchip',1)
    print(ia)

    next_moves = [[ia]]
    explored_layouts = set()
    #mn = 0
    #start_time = time()
    while next_moves:
        moves = next_moves.pop(0)
        ia = moves[-1]
        #if len(moves) != mn:
        #    print(f"explored: {len(explored_layouts)} - to explore: {len(next_moves)} - moves: {len(moves)} - time elapsed: {time() - start_time:.2f}  ")
        #    #start_time = time()
        #    mn = len(moves)
        if len(ia.floors[4] ^ ia.objects)  == 0:
            print('\n\nfound\n\n')
            break
        for nm in ia.next_possible_moves():
            if nm not in explored_layouts:
                next_moves.append(moves+[nm])
                explored_layouts.add(nm)

    #print(f"Moves: {len(moves)-1}")
    #for m in moves:
    #    print(m)
    #    #input()
    print(f"Moves: {len(moves)-1}")
