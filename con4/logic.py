"""Connect 4 logic"""
from board import GameBoard

def check_lat_win (board:GameBoard, i, j):
#Check if the slot (i,j) corresponds to a win in the vertical direction

	piece_count = 1 #keeps track of how many pieces are in a row of the same color, when it reaches 4 the game ends
	piece = board.piece
	pointer = i - 1 #current location
	while board.valid(pointer, j) and board[pointer, j] == piece: #while piece is same color as original and a valid board space
		piece_count += 1
		pointer -= 1
	pointer = i + 1
	while board.valid(pointer, j) and board[pointer, j] == piece:
		piece_count += 1
		pointer += 1

	#print("LAT:", piece_count)
	return piece_count >= 4

def check_long_win(board:GameBoard, i, j):
#Check if the slot (i,j) corresponds to a win in the horizontal direction
	piece_count = 1
	piece = board.piece
	pointer = j - 1
	while board.valid(i, pointer) and board[i, pointer] == piece:
		piece_count += 1
		pointer -= 1
	pointer = j + 1
	while board.valid(i, pointer) and board[i, pointer] == piece:
		piece_count += 1
		pointer += 1

	#print("LONG:", piece_count)
	return piece_count >= 4

def check_l_diag(board:GameBoard, i, j):

	piece_count = 1
	piece = board.piece
	lat_p = i + 1
	long_p = j - 1
	while board.valid(lat_p, long_p) and board[lat_p,long_p] == piece:
		piece_count += 1
		lat_p += 1
		long_p -= 1
	lat_p = i - 1
	long_p = j + 1
	while board.valid(lat_p, long_p) and board[lat_p,long_p] == piece:
		piece_count += 1
		lat_p += 1
		long_p -= 1

	#print("LDIAG:", piece_count)
	return piece_count >= 4

def check_r_diag(board:GameBoard, i , j):

	piece_count = 1
	piece = board.piece
	lat_p = i + 1
	long_p = j + 1
	while board.valid(lat_p, long_p) and board[lat_p,long_p] == piece:
		piece_count += 1
		lat_p += 1
		long_p += 1
	lat_p = i - 1
	long_p = j - 1
	while board.valid(lat_p, long_p) and board[lat_p,long_p] == piece:
		piece_count += 1
		lat_p -= 1
		long_p -= 1

	#print("RDIAG:", piece_count)
	return piece_count >= 4


def check_all_wins(board:GameBoard, i, j):
	return check_lat_win(board,i,j) or check_long_win(board,i,j) or check_r_diag(board,i,j) or check_l_diag(board,i,j)
"""
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
"""