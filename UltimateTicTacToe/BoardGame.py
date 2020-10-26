from Board import Board
from Player import Player

class BoardGame():

    def __init__(self, n, startx, starty):
        
        self.board = Board(n)
        self.p1 = Player("p1", "*")
        self.p2 = Player("p2", "o")
        self.currentPlayer = self.p1
        self.currentBoard = [startx, starty]

    def allowed(self, x, y , i , j):
        if not self.board.isAlreadyFilled(x,y,i,j):
            if not self.currentBoard or (x == self.currentBoard[0] and y == self.currentBoard[1]):
                return True
        return False

    def setValue(self, x, y,i,j):
        if self.allowed(x,y, i, j):
            
            self.board.write(x , y , self.currentPlayer.returnSymbol(), i, j)

            if self.currentPlayer.returnName() == "p1":
                self.currentPlayer = self.p2
            else:
                self.currentPlayer = self.p1

        else:
            print("Please enter a different location")

    
            


        

        

    

        

    

        

    





