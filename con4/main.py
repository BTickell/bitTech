from board import *
from logic import *

def main():
	row_num = input("Enter the number of rows [default: 6] : ")
	if row_num == "":
		row_num = 6
	col_num = input("Enter the number of columns [default: 7] : ")
	if col_num == "":
		col_num = 7
	board = GameBoard(row_num, col_num)
	logic = ConnectLogic(board)
	not_end = True
	print(board)
	while not_end:
		try:
			com = input("Enter a command: ")
			if com == "q":
				break
			pos = board.add_piece(eval(com)) # Gives us the most recent position of the piece placed.
			print(board)
			i, j = pos
			if logic.check_vert_win(i, j):
				print("TEMPORARY CONGRATZ METHOD")
			board.player_swap()
		except:
			pass
main()