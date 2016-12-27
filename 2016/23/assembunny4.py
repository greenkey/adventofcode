import sys

class AssembunnyInterpreter():
    def __init__(self,registers=None):
        self.register = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0
        }

    def set_registers(self,registers):
        self.register = {
            'a': int(registers[0]),
            'b': int(registers[1]),
            'c': int(registers[2]),
            'd': int(registers[3])
        }

    def eval(self,val):
        try:
            return int(val)
        except ValueError:
            return self.register[val]

    def compile(self,code):
        self.code = list()
        for line in code:
            if line:
                if line[0] == 'cpy':
                    line[0] = self._cpy
                elif line[0] == 'inc':
                    line[0] = self._inc
                elif line[0] == 'dec':
                    line[0] = self._dec
                elif line[0] == 'jnz':
                    line[0] = self._jnz
                elif line[0] == 'tgl':
                    line[0] = self._tgl
                elif line[0] == 'add':
                    line[0] = self._add
                else:
                    continue

                if line[1] not in self.register.keys():
                    line[1] = int(line[1])
                try:
                    if line[2] not in self.register.keys():
                        line[2] = int(line[2])
                except IndexError:
                    line.append(0)

                self.code.append(line)

    def _cpy(self,x,y):
        self.register[y] = self.eval(x)
    def _add(self,x,y):
        self.register[y] += self.eval(x)
    def _inc(self,x,y):
        self.register[x] += 1
    def _dec(self,x,y):
        self.register[x] -= 1
    def _jnz(self,x,y):
        if self.eval(x) > 0:
            self.i += self.eval(y)-1
    def _tgl(self,x,y):
        #print("tgl",x,end=' - ')
        try:
            tgl = self.code[self.i+self.eval(x)]
            #print(self.i+self.eval(x), tgl[0].__name__," "*30)
            if tgl[0] == self._inc:
                tgl[0] = self._dec
            elif tgl[0] == self._dec:
                tgl[0] = self._inc
            elif tgl[0] == self._jnz:
                tgl[0] = self._cpy
            elif tgl[0] == self._cpy:
                tgl[0] = self._jnz
            #print("New code:\n{}".format(self.get_code()))
        except IndexError:
            pass

    def execute(self):
        self.i = 0
        #ctr = 0
        while self.i < len(self.code):
            line = self.code[self.i]
            #if ctr%(2**20) == 0:
            #    print(self.i, self.register, " "*30,end='\r')

            line[0](line[1],line[2])

            self.i += 1
            #ctr += 1

    def get_code(self):
        return '\n'.join(' '.join([str(p) for p in code]))



with open(sys.argv[1],'r') as f:
    code = [l.strip().split() for l in f.read().split('\n')]

ai = AssembunnyInterpreter()

if len(sys.argv)>=2:
    ai.set_registers(sys.argv[2].split(','))

ai.compile(code)

ai.execute()

print(ai.register," "*30)
