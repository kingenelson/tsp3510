import random

fp = open("thousand_nodes.txt", "w")
for i in range(1000):
	x = random.uniform(0, 30000)
	y = random.uniform(0, 30000)
	fp.write(str(i+1)+" "+f"{x:.4f}"+" "+f"{x:.4f}"+'\n')
