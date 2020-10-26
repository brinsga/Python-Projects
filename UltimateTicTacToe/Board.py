from Cell import Cell

class Board():
	"""
	This Board stores the 9 cells in the ultimate tic-tac toe and
	players have direct access to the boards
	"""
	def __init__(self, n):

		self.n = n
		self.board = []

		for i in range(n):
			self.board.append([])
			for j in range(n):
				self.board[i].append(Cell(self.n))

		self.boardState = [[None for i in range(n)] for j in range(n)]

	def printBoard(self):
		print("\n")
		for i in range(self.n):
			for j in range(self.n):
				string = ""
				for z in range(self.n):
					for val in self.board[i][j].returnState()[z]:
						string += str(val) + " "
					string += "     "
				print(string)
			print("\n\n") 


	def write(self,x,y,symbol,i, j):
		self.board[i][j].addSymbol(symbol,x,y)
		self.boardState[i][j] = self.board[i][j].isComplete(symbol)


	def isAlreadyFilled(self,x,y,i,j):
		return self.board[i][j].alreadyFilled(x,y)

	def gameWon(self, symbol):

		diagonal = []

		for i in range(3):
			if self.boardState[i:i+1][:].count(symbol) == 3 or self.boardState[:][i:i+1].count(symbol) == 3:
				return symbol
			diagonal.append(self.boardState[i][i])

		if (diagonal.count(symbol)) == 3:
			return symbol

		count = 0
		for i in range(3):
			for j in range(3):
				if self.boardState[i][j] == "T":
					count +=1

		if count == 9:
			return "Tie"

		return None


	def getBoard(self):
		return self.board


b = Board(3)
b.printBoard()








