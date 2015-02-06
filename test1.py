import pygame, sys
from pygame.locals import *


TILE_HEIGHT = 32
TILE_WIDTH = 32
SCREEN_HEIGHT = 11
SCREEN_WIDTH = 11



def check_empty(x, y, x_o, y_o, m_w, m_h):
	if get_tile(x, y, x_o, y_o, m_w, m_h) == 0:
		return True
	return False
	
def get_tile(x, y, x_o, y_o, m_w, m_h):
	return map[(m_w * (y + y_o)) + x + x_o]




pygame.init()

screen = pygame.display.set_mode((352,352))
pygame.display.set_caption("test")

ball = pygame.image.load("blue.png").convert()
black = pygame.image.load("black.png").convert()
white = pygame.image.load("white.png").convert()



b_x = 5
b_y = 5

map = [1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,1,1,0,1,0,0, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,1,0,0,0,1, 0,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,0,1,0,0,1, 0,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,0,0,1,0,1, 1,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,0,0,0,1,0, 1,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,1,1,0,0,0,0,0,0, 1,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,0,0,0,0,1,0,1,1, 1,0,0,0,0,0,0,0,0,0, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,    
	   1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1]

map_height = 20
map_width = 30

x_offset = 3
y_offset = 7

screen.fill(pygame.Color(255, 0, 0))

while 1:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				if check_empty(b_x - 1, b_y, x_offset, y_offset, map_width, map_height):
					if x_offset > 0:
						x_offset -= 1
					else:
						b_x -= 1
			elif event.key == K_RIGHT:
				if check_empty(b_x + 1, b_y, x_offset, y_offset, map_width, map_height):
					if x_offset < map_width - SCREEN_WIDTH:
						x_offset += 1
					else:
						b_x += 1
			elif event.key == K_UP:
				if check_empty(b_x, b_y - 1, x_offset, y_offset, map_width, map_height):
					if y_offset > 0:
						y_offset -= 1
					else:
						b_y -= 1
			elif event.key == K_DOWN:
				if check_empty(b_x, b_y + 1, x_offset, y_offset, map_width, map_height):
					if y_offset < map_height - SCREEN_HEIGHT:
						y_offset += 1
					else:
						b_y += 1
				
		
		
	screen.fill(pygame.Color(255, 0, 0))
	
	for i in range(0, SCREEN_HEIGHT):
		for j in range(0, SCREEN_WIDTH):
			if get_tile(j, i, x_offset, y_offset, map_width, map_height):
				screen.blit(black, (TILE_WIDTH * j, TILE_HEIGHT * i))
			else:
				screen.blit(white, (TILE_WIDTH * j, TILE_HEIGHT * i))
	
	screen.blit(ball, (b_x * TILE_WIDTH, b_y * TILE_HEIGHT))
	pygame.display.update()
	
	

