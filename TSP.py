
#return list of tuples containing id, x, and y coordinates
def readFile(fileName):
	fp = open(fileName, 'r')
	x_y = []
	for line in fp:
		lines = line.split()
		#appends a new tuple with id, x, and y coordinates into list
		x_y.append((int(lines[0]), int(lines[1]), int(lines[2])))
	return x_y