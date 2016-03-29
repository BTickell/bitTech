from main import *
import pygame
from board import *
from logic import *

from pygame.locals import *

pygame.init()
pygame.font.init()

new_display = pygame.display.set_mode((1193,961))

img = pygame.image.load('graphics/con4.png')
r_piece = pygame.image.load('graphics/red_piece.png').convert_alpha() #image for pieces
b_piece = pygame.image.load('graphics/blue_piece.png').convert_alpha()

pygame.display.set_caption('Connect 4')

board = GameBoard(6, 7) #keeps track of pieces and logic behind the screen
width = 170.4286 #dimensions for each individual slot on the board
height = 160.17
grid = [] #array that keeps track of how many pieces are in each column visually
for i in range(7): #when an element in the grid is 1,it means the gui already displays piece there
	grid.append(0)

game_over = False

new_display.blit(img, (0,0))
pygame.display.update()
while True:
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONUP:
			if game_over:
				break
			pos = pygame.mouse.get_pos()
			col = pos[0] // width #rounds pixel pos clicked to closest actual slot
			if grid[int(col)] < 6:
				grid[int(col)] += 1
				to_place = board.add_piece(int(col)) #lowest non_empty row in clicked column
				if board.current == 1:
					new_display.blit(r_piece, (col*width + 27, to_place[0]*height + 30))
				else:
					new_display.blit(b_piece, (col*width + 27, to_place[0]*height + 30))

				if check_all_wins(board, to_place[0], to_place[1]):
					winner = eval("board.player" + str(board.current))
					font1 = pygame.font.SysFont("comicsansms", 64)
					game_message = font1.render(winner + " has won!", True, (55,55,0))
					new_display.blit(game_message, (400,400))
					game_over = True
				
				board.player_swap()
				
				pygame.display.flip()
		if event.type == QUIT:
			pygame.quit()
