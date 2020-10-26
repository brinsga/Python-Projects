class Cell():
	"""
	The cell class stores information of a single tic-tac-toe cell

	"""
	def __init__(self, n):

		self.n = n
		self.components = [["/" for i in range(self.n)] for j in range(self.n)]
		self.available = n*n

	def __str__(self):

		string = ""

		for i in range(self.n):
			for j in range(self.n):
				string+= (str(self.components[i][j]) + " ")
			string += ("\n")

		return string

	def addSymbol(self, symbol, x, y):
		
		self.components[x][y] = symbol
		self.available -=1

	
	def alreadyFilled(self, x, y):
		if self.components[x][y] != "/":
			return True
		return False


	def isComplete(self, symbol):

		if self.available == 0:
			return False

		diagonal = []

		for i in range(3):
			if self.components[i:i+1][:].count(symbol) == 3 or self.components[:][i:i+1].count(symbol) == 3:
				return True
			diagonal.append(self.components[i][i])

		if (diagonal.count(symbol)) == 3:
			return True

		return None


	def returnState(self):
		return self.components
