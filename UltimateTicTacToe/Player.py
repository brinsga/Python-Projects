class Player():
	"""
	This class stores information about each player and the simple
	they are associated with. 
	"""

	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol

	def returnName(self):
		return self.name

	def returnSymbol(self):
		return self.symbol