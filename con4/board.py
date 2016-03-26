""""Connect 4 Game"""

class GameBoard:
	"""Holds a list of lists"""
	pieces = ["-", "r", "b"] #Pieces that are valid: "-" --> Empty slot, "b" --> blue piece, "r" --> red piece
	def __init__(self, N, M):
		self.grid = [["-" for i in range(M)] for i in range(N)]
		self._row = N
		self._col = M
		self.player1 = "Red"
		self.player2 = "Blue"
		self.current = 1
		self.piece = "r" 

	def player_swap(self):
		self.current = 3 - self.current
		if self.piece == "r":
			self.piece = "b"
		else:
			self.piece = "r"

	def valid(self, N, M):
		if N < self._row and N >= 0:
			if M < self._col and M >= 0:
				return True 
		return False

	def is_empty(self, row:int, col:int):
		return self[row, col] == "-"

	def __getitem__(self, pos:(int, int)):
		row, col = pos
		assert 0 <= row and row < self._row, "GameBoard::get_piece:: Row is out of range!"
		assert 0 <= col and row < self._col, "GameBoard::get_piece:: Column is out of range!"
		return self.grid[row][col]

	def __setitem__(self, pos:(int, int), val):
		row, col = pos
		assert 0 <= row and row < self._row, "GameBoard::get_piece:: Row is out of range!"
		assert 0 <= col and row < self._col, "GameBoard::get_piece:: Column is out of range!"
		self.grid[row][col] = val
 
	def add_piece(self, target: int):
		assert 0 <= target < self._col, "GameBoard::add_piece:: Column is out of range!"
		assert self.is_empty(0,target), "GameBoard::add_piece:: Column is full!"
		to_place = self._row - 1

		while not self.is_empty(to_place, target):
			to_place -= 1

		self[to_place, target] = self.piece
		return to_place, target




	"""Built in operator functions <0v3rl04ded>""" 
	def __str__(self):
		result = ""
		for row in self.grid:
			for element in row:
				result += element + " "
			result += '\n'
		return result






