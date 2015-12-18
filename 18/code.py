import copy

class ConwayGameOfLife():
    def __init__(self,board_size):
        (x,y) = map(lambda x: int(x), board_size.split("x"))
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
