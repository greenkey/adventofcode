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
                elif line[0] == 'out':
                    line[0] = self._out
                else:
                    continue

                if line[1] not in self.register.keys():
                    line[1] = int(line[1])
                try:
                    if line[2] not in self.register.keys():
                        line[2] = int(line[2])
                except IndexError:
                    pass

                self.code.append(line)

    def _cpy(self,x,y):
        self.register[y] = self.eval(x)
    def _inc(self,x):
        self.register[x] += 1
    def _dec(self,x):
        self.register[x] -= 1
    def _jnz(self,x,y):
        if self.eval(x) > 0:
            self.i += self.eval(y)-1
    def _out(self,x):
        return self.eval(x)+1
    def _tgl(self,x):
        try:
            tgl = self.code[self.i+self.eval(x)]
            #print(self.i+self.eval(x), tgl[0].__name__," "*30)
            if tgl[0] == self._inc:
                tgl[0] = self._dec
            elif len(tgl) == 2:
                tgl[0] = self._inc
            elif tgl[0] == self._jnz:
                tgl[0] = self._cpy
            elif len(tgl) == 3:
                tgl[0] = self._jnz
        except IndexError:
            pass

    def execute(self):
        self.i = 0
        while self.i < len(self.code):
            line = self.code[self.i]
            #print(self.i, self.register, " "*30,end='\r')

            x = None

            try:
                x = line[0](line[1],line[2])
            except IndexError:
                x = line[0](line[1])

            if x:
                yield x

            self.i += 1



with open(sys.argv[1],'r') as f:
    code = [l.split() for l in f.read().split('\n')]

ai = AssembunnyInterpreter()


ai.compile(code)

print("Now the program will try to execute the assembunny code until it generates a 1-0 infinite sequence.")
print("When it stops, the last line is the number!")
input("Press enter when ready")

a = 0
found = False
while not found:
    print(a)
    ai.set_registers([a,0,0,0])
    prev = 3
    i = 0
    for x in ai.execute():
        print(x,end='')
        if prev == x and i>10:
            found = False
            print()
            break
        prev = x
        i += 1
    a += 1

print(ai.register," "*30)
