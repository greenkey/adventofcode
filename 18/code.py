import copy

class ConwayGameOfLife():
    def __init__(self,board_size):
        (x,y) = map(lambda x: int(x), board_size.split("x"))
        self.x = x
        self.y = y
        self.matrix = [[False for a in range(x)] for a in range(y)] 

    def setBoardFromString(self,board,line_ending="\n",on_char="1",off_char="0"):
        lines = board.split(line_ending)
        newMatrix = copy.deepcopy(self.matrix)
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if lines[x][y] == on_char:
                    newMatrix[x][y] = 1
                elif lines[x][y] == off_char:
                    newMatrix[x][y] = 0
                else:
                    raise Error("Character {} not expected".format(lines[x][y]))
        self.matrix = newMatrix
    
    def getBoardString(self,line_ending="\n",on_char="1",off_char="0"):
        return line_ending.join( map(lambda line: "".join(map( lambda c: on_char if c == 1 else off_char ,line )), self.matrix) )

    def advanceOne(self):
        newMatrix = copy.deepcopy(self.matrix)
        for x in range(self.x):
            for y in range(self.y):
                from_x = max(0,x-1)
                to_x = min( self.x, x+2 )
                from_y = max(0,y-1)
                to_y = min( self.y, y+2 )
                neighbours = map(lambda line: line[ from_y : to_y ],self.matrix)[ from_x : to_x ]
                on_neighbours = sum(map(lambda line: sum(line), neighbours)) - self.matrix[x][y]
                if self.matrix[x][y] == 1 and on_neighbours not in (2,3):
                    newMatrix[x][y] = 0
                if self.matrix[x][y] == 0 and on_neighbours == 3:
                    newMatrix[x][y] = 1
        self.matrix = newMatrix

    def countOn(self):
        return sum(map(lambda line: sum(line), self.matrix))        

    def advance(self,of):
        for i in range(of):
            self.advanceOne()


if __name__ == "__main__":

    cgof = ConwayGameOfLife("100x100")

    # get first configuration
    with open('input', 'r') as container_list:
        cgof.setBoardFromString(board=container_list.read(),on_char="#",off_char=".")
    print(cgof.getBoardString(on_char="#",off_char="."))
    cgof.advance(of=100)
    print("Calculating...")
    print(cgof.getBoardString(on_char="#",off_char="."))
    print("The sum of on lights: {}".format(cgof.countOn()))