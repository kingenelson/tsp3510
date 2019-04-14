import sys
import math
import random
import copy
import datetime


def input():
    filename = str(sys.argv[1])
    output = str(sys.argv[2])
    max_time = int(sys.argv[3])
    return [filename, output, max_time]

class Graph:
    """docstring for Graph"""
    def __init__(self, fileName):
        # get points in from of [(ID, (X, Y)), ...]
        fp = open(fileName, 'r')
        #self.maxTime = maxTime
        x_y = []
        for line in fp:
            lines = line.split()
        #appends a new tuple with id, x, and y coordinates into list 
            x_y.append((int(float(lines[0])), int(float(lines[1])), int(float(lines[2]))))
        #creates dictionary of distances between all points
        self.pairMatrix = [[] for x in range(len(x_y))]
        for i in range(len(x_y)):
            for j in range(len(x_y)):
                self.pairMatrix[i].append(int(math.sqrt((x_y[i][1]-x_y[j][1])**2 + (x_y[i][2]-x_y[j][2])**2)))

    def getPairMatrix(self):
        return self.pairMatrix


# Runs 2-opt on a graph
def twoOpt(graph, route):
    # Generate a random cycle and calcs its distance
    pm = graph.getPairMatrix()
    # route = list(range(1, len(pm)))
    # print(route)
    d = distance(route, pm)
    # print(d)
    t = 0
    tempd = d
    while (d > 28000 and t <= 200):
        for i in range(0, len(route) - 1):
            for k in range(i + 1, len(route)):
                # if k >= len(route):
                #     k -= len(route)
                r0 = route[0:i]
                r1 = route[i:k]
                r1 = r1[::-1]
                r2 = route[k:]
                r = r0 + r1 + r2
                newd = distance(r, pm)
                if (newd < d):
                    d = newd
                    route = r
        t += 1
        if (d == tempd and t > 5):
            break
    return route

def distance(route, pairMatrix):
    dist = 0
    # for every node in tour - 1
    for i in range(0, len(route)):
        # print("--", route[i])
        if i + 1 >= len(route):
            dist += pairMatrix[route[i]][route[0]]
        else:
            # print(i, route[i])
            dist += pairMatrix[route[i]][route[i + 1]]
    return dist

def main():
    start = datetime.datetime.now()
    params = input()
    g = Graph(params[0])

    pm = g.getPairMatrix()
    ir = list(range(1, len(pm)))
    r = twoOpt(g, ir)
    d = distance(r, g.getPairMatrix())

    start = datetime.datetime.now()
    while (datetime.datetime.now() - start).seconds < 170:
        rr = copy.deepcopy(ir)
        random.shuffle(rr)
        # print(rr)
        tr = twoOpt(g, rr)
        rd = distance(tr, g.getPairMatrix())
        if (rd < d):
            d = rd
            r = tr
    print(d)
    print(r)
    fp = open(params[1], 'w')
    fp.write(str(d) + "\n")
    for city in r:
        fp.write(str(city) + " ")
    fp.write(str(r[0]))
    print((datetime.datetime.now() - start).seconds)






if __name__ == "__main__":
    main()
 
