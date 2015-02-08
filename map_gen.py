
"""
Layout of maps should be:
	map data, width, height

"""
def gen_filled_map(w, h):

	map = []
	for i in range(0, w * h):
		map.append(1)
	map.append(w)
	map.append(h)
	return map

def empty_a_room(m, x, y, w, h):
	for i in range(y, y+h):
		for j in range(x, x+w):
			m[i * m[-2] + j] = 0
	
