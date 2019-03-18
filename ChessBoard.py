from ChessPieces import *

class ChessBoard:

    def __init__(self, size):
        self.size = size
        self.board = [["0"] * size for i in range(size)]

    #Place the chess pieces in the default order
    def setDefaultPositions(self):
        # For testing purpose
        self.board[0][1] = Pawn("White", self.board, 0, 1)


    def __str__(self):

        output = ""
        for line in self.board:
            string = "["
            for block in line:
                if block != "0":
                    string += block.symbol
                else:
                    string += block
                string += ", "
            output += string[:-2] + "]\n"
        return output


x = ChessBoard(8)
x.setDefaultPositions()

print(x)