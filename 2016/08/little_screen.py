import sys

class tiny_display():

    def __init__(self,wide,tall):
        self.display = [[0 for x in range(wide)] for y in range(tall)]

    def execute(self,command):
        tokens = command.split()
        getattr(self,tokens[0])(tokens[1:])

    def light_on_pixel(self,x,y):
        self.display[x][y] = 1

    def rect(self,size):
        (wide,tall) = [int(x) for x in size[0].split('x')]
        [[self.light_on_pixel(x,y) for y in range(wide)] for x in range(tall)]

    def rotate(self,parameters):
        (k,v) = parameters[1].split('=')
        assert parameters[2]=='by'
        n = int(parameters[3])
        if parameters[0]=="row":
            assert k=='y'
            y = int(v)
            self.display[y] = self.display[y][-n:] + self.display[y][:-n]
        if parameters[0]=="column":
            assert k=='x'
            x = int(v)
            temp_display = [l[:] for l in self.display[:]]
            for i in range(len(self.display)):
                self.display[i][x] = temp_display[(i-n)%(len(self.display))][x]

    def get_string_display(self,p0='.',p1='#',nl='\n'):
        return nl.join([''.join([p0 if p==0 else p1 for p in l]) for l in self.display])

    def get_lit_pixels(self):
        return sum([sum(l) for l in self.display])

with open(sys.argv[1],'r') as f:
    d = tiny_display(50,6)
    [d.execute(l.strip()) for l in f]
print(d.get_string_display())
print(d.get_lit_pixels())
