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

    def gameWon(self, symbol= self.currentPlayer.returnSymbol):
        result = self.board.gameWon(symbol)

        if result:
            if self.board.gameWon == "Tie":
                print("The Game has been tied")
            else:
                if result == "*":
                    print("Player1 Won")
                else:
                    print("Player2 Won")
            
            return True

        else:
            return False


    def changePlayer(self):
        if self.currentPlayer.returnName() == "p1":
                self.currentPlayer = self.p2
        else:
                self.currentPlayer = self.p1


    def setValue(self, x, y, i, j):
        if self.allowed(x,y, i, j):
            self.board.write(x , y , self.currentPlayer.returnSymbol(), i, j)
            return True

        else:
            print("Please enter a different location")
            return False


    

    

    

    
            


        

        

    

        

    

        

    





