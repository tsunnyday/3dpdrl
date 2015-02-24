import pygame, sys
import map_gen
from pygame.locals import *


TILE_HEIGHT = 32
TILE_WIDTH = 32
SCREEN_HEIGHT = 11
SCREEN_WIDTH = 11

MAP_HEIGHT = 300
MAP_WIDTH = 200

BALL_ON_SCREEN_X = 5
BALL_ON_SCREEN_Y = 5

def check_empty(x_o, y_o, m_w, m_h):
	if get_tile(x_o, y_o, m_w, m_h) in [0,7]:
		return True
	return False
	
def get_tile(x_o, y_o, m_w, m_h):
	return map[(m_w * (y_o)) + x_o]




pygame.init()

screen = pygame.display.set_mode((352,352))
pygame.display.set_caption("test")

ball = pygame.image.load("blue.png").convert()
black = pygame.image.load("black.png").convert()
white = pygame.image.load("white.png").convert()
brown = pygame.image.load("brown.png").convert()
stairs = pygame.image.load("stairs.png").convert()




map = map_gen.gen_filled_map(MAP_WIDTH, MAP_HEIGHT)
flag_coor = map_gen.fill_with_rooms(map)



x_offset = map[-4] - 5
y_offset = map[-3] - 5




screen.fill(pygame.Color(255, 0, 0))

while 1:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			
			if event.key == K_LEFT:
				if check_empty(BALL_ON_SCREEN_X + x_offset - 1, BALL_ON_SCREEN_Y + y_offset, MAP_WIDTH, MAP_HEIGHT):
						x_offset -= 1
					
					
			elif event.key == K_RIGHT:
				if check_empty(BALL_ON_SCREEN_X + x_offset + 1, BALL_ON_SCREEN_Y + y_offset, MAP_WIDTH, MAP_HEIGHT):
						x_offset += 1
					
			elif event.key == K_UP:
				if check_empty(BALL_ON_SCREEN_X + x_offset, BALL_ON_SCREEN_Y + y_offset - 1, MAP_WIDTH, MAP_HEIGHT):
						y_offset -= 1
				
			elif event.key == K_DOWN:
				if check_empty(BALL_ON_SCREEN_X + x_offset, BALL_ON_SCREEN_Y + y_offset + 1, MAP_WIDTH, MAP_HEIGHT):
						y_offset += 1
			elif event.key == K_RSHIFT:		
				print "POS:" + str(BALL_ON_SCREEN_X + x_offset) + "," + str(BALL_ON_SCREEN_Y + y_offset)
			elif event.key == K_RETURN:
				print "FLAG:" + str(flag_coor)
		
		
	if(get_tile(BALL_ON_SCREEN_X + x_offset, BALL_ON_SCREEN_Y + y_offset, MAP_WIDTH, MAP_HEIGHT) == 7):
		map = map_gen.gen_filled_map(MAP_WIDTH, MAP_HEIGHT)
		flag_coor =  map_gen.fill_with_rooms(map)



		x_offset = map[-4] - 5
		y_offset = map[-3] - 5
	
		
		
		
	screen.fill(pygame.Color(255, 0, 0))
	
	for i in range(0, SCREEN_HEIGHT):
		for j in range(0, SCREEN_WIDTH):
			t = get_tile(j + x_offset, i + y_offset, MAP_WIDTH, MAP_HEIGHT)
			if  t == 1:
				screen.blit(black, (TILE_WIDTH * j, TILE_HEIGHT * i))
			elif t == 2:	
					screen.blit(black, (TILE_WIDTH * j, TILE_HEIGHT * i))
			elif t == 3:	
					screen.blit(ball, (TILE_WIDTH * j, TILE_HEIGHT * i))	
			elif t == 7:
					screen.blit(stairs, (TILE_WIDTH * j, TILE_HEIGHT * i))
			else:
				screen.blit(white, (TILE_WIDTH * j, TILE_HEIGHT * i))
	
	screen.blit(ball, (BALL_ON_SCREEN_X * TILE_WIDTH, BALL_ON_SCREEN_Y * TILE_HEIGHT))
	pygame.display.update()
	
	

