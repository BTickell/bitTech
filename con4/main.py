from con4 import *

def main():
	row_num = input("Enter the number of rows [default: 6] : ")
	if row_num == "":
		row_num = 6
	col_num = input("Enter the number of columns [default: 7] : ")
	if col_num == "":
		col_num = 7
	board = GameBoard(row_num, col_num)

main()