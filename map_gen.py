import random

"""
Layout of maps should be:
	map data, start_x, start_y, width, height

"""

ROOM_MIN = 5
ROOM_MAX = 15
HALL_MIN = 6
HALL_MAX = 20


def gen_filled_map(w, h):

	map = []
	for i in range(0, w * h):
		map.append(1)
	map.append(0)
	map.append(0)
	map.append(w)
	map.append(h)
	return map

def gen_normal_int(least, most):
	mean = (most - least)/ 2.0
	stddev = (most - mean) / 3.0
	num = most + 1
	while ((num > most) or (num < least)):
		num = round(random.gauss(mean, stddev)) 
	return int(num)

def convert_int_to_x_and_y(m, i):
	x = i % m[-2]
	y = (i - (i % m[-2])) / m[-2]
	return [x, y] 

"""  Okay, so  basically, the ideas is, empty out a random room.  This is the start room.  Now Pick a random wall.  At this wall,
generate a hallway that ends in another room.  Repeat for as long as u want.





"""
def fill_with_rooms(m):
	
	l = empty_a_room(m, m[-2]/2, m[-1]/2, gen_normal_int(ROOM_MIN, ROOM_MAX), gen_normal_int(ROOM_MIN, ROOM_MAX))
	m[-4] = l[0]
	m[-3] = l[1]
	
	for i in range(0, 10):
		gen_next_node(m)
	
	
def gen_next_node(m):	
	p = pick_wall(m)
	wall_good = False
	hl = gen_normal_int(HALL_MIN, HALL_MAX)
	rx = gen_normal_int(ROOM_MIN, ROOM_MAX)
	ry = gen_normal_int(ROOM_MIN, ROOM_MAX)
	loc = convert_int_to_x_and_y(m, p)
	#check dir
	if m[p - 1] == 0:
		print "left"
		m[p] = 1
		wall_good = empty_a_room(m, loc[0] + 1, loc[1], hl, 1)
		m[p + hl + 1] = 1
		print empty_a_room(m, loc[0] + hl + 1, loc[1] - (ry/2), rx, ry)
		m[p + hl] = 0
			
		
		
	elif m[p + 1] == 0:
		print "right"
		m[p] = 1
		wall_good = empty_a_room(m, loc[0] - hl, loc[1], hl, 1)
		m[p - hl - 1] = 1
		print empty_a_room(m, loc[0] - hl - rx, loc[1] - (ry/2), rx, ry)
		m[p - hl] = 0
		
	else:
		
		if(m[(loc[1] + 1) * m[-2] + loc[0]] == 0):
			print "down"
			m[p] = 1
			wall_good = empty_a_room(m, loc[0], loc[1] - hl, 1, hl)
			m[(loc[1] - hl - 1) * m[-2] + loc[0]] = 1
			print empty_a_room(m, loc[0] - (rx/2), loc[1] - hl - ry - 1, rx, ry) 
			m[(loc[1] - hl - 1) * m[-2] + loc[0]] = 0
			
		else:
			print "up"
			m[p] = 1
			wall_good = empty_a_room(m, loc[0], loc[1] + 1, 1, hl)
			m[(loc[1] + hl + 1) * m[-2] + loc[0]] = 1
			print empty_a_room(m, loc[0] - (rx/2), loc[1] + hl + 2, rx, ry)
			m[(loc[1] + hl + 1) * m[-2] + loc[0]] = 0
			
			
	print "wall_good:" + str(wall_good)		
	if(wall_good):
		m[p] = 0	
		
def empty_a_room(m, x, y, w, h):
	if x > 0 and y > 0 and x + w < m[-2] and y + h < m[-1]:
		# requires a space of w + 2, h + 2 (one more on each side)
		for i in range(y - 1, y + h + 1):
			for j in range(x, x + w):
				if m[i * m[-2] + j] != 1:
					return False
		for i in range(y, y + h):
			if m[i + m[-2] + x - 1] != 1:
				return False
			if m[i + m[-2] + x + w + 1] != 1:
				return False	
				
		
		for i in range(y, y+h):
			m[i * m[-2] + x - 1] = 2
			m[i * m[-2] + x + w] = 2
			for j in range(x, x + w):
				m[i * m[-2] + j] = 0
				m[(y - 1) * m[-2] + j] = 2
				m[(y + h) * m[-2] + j] = 2
		
		
		return [x + (w/2), y + (h/2)]
	else:
		return False

def pick_wall(m):
	pick = -1
	while m[pick] != 2:
		pick = random.randint(0, len(m) - 5)
	m[pick] = 3
	return pick
	
	
def check_wall(m, x, y):
	if m[y * m[-2] + x + 1] == 0:
		return True
	elif m[y * m[-2] + x - 1] == 0:
		return True
	elif m[(y + 1) * m[-2] + x] == 0:
		return True
	elif m[(y - 1) * m[-2] + x] == 0:
		return True
	return False
	
	
