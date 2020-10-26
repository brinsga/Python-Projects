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


	def won


b = Board(3)
b.printBoard()








