from main import *
import pygame

from pygame.locals import *

pygame.init()

new_display = pygame.display.set_mode((300,300))

pygame.display.set_caption('Connect 4')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()