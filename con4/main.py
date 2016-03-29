from board import *
from logic import *

def is_int(val):
	try:
		assert type(eval(val)) == int
	except:
		return False
	return True

def main():
	row_num = input("Enter the number of rows [6]: ")
	if row_num == "":
		row_num = "6"
	col_num = input("Enter the number of columns [7]: ")
	if col_num == "":
		col_num = "7"
	board = GameBoard(eval(row_num), eval(col_num))
	not_end = True
	print(board)
	while not_end:
		try:
			com = input("Enter a command: ")
			if com == "q":
				break
			assert is_int(com)
			pos = board.add_piece(eval(com) - 1) # Gives us the most recent position of the piece placed and adds a new piece to the board.
			print(board)
			#i, j = pos
			if check_all_wins(board, pos[0], pos[1]):
				print("TEMPORARY CONGRATZ METHOD")
			board.player_swap()
		except AssertionError as e:
			print("An ERROR occurred, please try again")