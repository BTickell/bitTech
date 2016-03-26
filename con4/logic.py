"""Connect 4 logic"""

class ConnectLogic:
	def __init__(self, board):
		self.board = board
	def check_vert_win(self, i, j):
	#Check if the slot (i, j) corresponds to a win in the vertical direction
		piece_count = 1
		board = self.board
		piece = board.piece
		pointer = i - 1
		while board.valid(pointer, j) and board[pointer, j] == piece:
			piece_count += 1
			pointer -= 1
		pointer = i + 1
		while board.valid(pointer, j) and board[pointer, j] == piece:
			piece_count += 1
			pointer += 1

		if piece_count == 4:
			return True
		return False
