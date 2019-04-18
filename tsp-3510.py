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
        # Makes a list of IDs
        self.IDs = []
        for i in range(len(x_y)):
            self.IDs.append(x_y[i][0])

    def getPairMatrix(self):
        return self.pairMatrix

    def getIDs(self):
        return self.IDs


# Runs 2-opt on a graph
def twoOpt(graph, route, max_time, start):
    # Generate a random cycle and calcs its distance
    pm = graph.getPairMatrix()
    d = distance(route, pm, max_time, start)
    t = 0
    tempd = d
    while (t <= 200):
        for i in range(0, len(route) - 1):
            for k in range(i + 1, len(route)):
                # if k >= len(route):
                #     k -= len(route)
                r0 = route[0:i]
                r1 = route[i:k]
                r1 = r1[::-1]
                r2 = route[k:]
                r = r0 + r1 + r2
                if (datetime.datetime.now() - start).seconds >= max_time - 10:
                    return route
                newd = distance(r, pm, max_time, start)
                if (newd < d):
                    d = newd
                    route = r
        t += 1
        if ((d == tempd and t > 5) or (datetime.datetime.now() - start).seconds >= max_time - 2):
            break
    return route

def distance(route, pairMatrix, max_time, start):
    dist = 0
    # for every node in tour
    for i in range(0, len(route)):
        if (datetime.datetime.now() - start).seconds >= max_time - 2:
            return -1
        if (i) >= (len(route) - 1):
            # last node to first node
            dist += pairMatrix[route[i] - 1][route[0] - 1]
        else:
            # node[i] to node[i + 1]
            dist += pairMatrix[route[i] - 1][route[i + 1] - 1]
    return dist

def main():
    start = datetime.datetime.now()
    params = input()
    g = Graph(params[0])
    max_time = params[2]

    pm = g.getPairMatrix()
    ir = g.getIDs()
    r = ir
    d = distance(r, g.getPairMatrix(), max_time, start)
    print("after int dist", (datetime.datetime.now() - start).seconds)

    while (datetime.datetime.now() - start).seconds < params[2] - 10:
        rd = d
        rr = copy.deepcopy(ir)
        random.shuffle(rr)
        tr = twoOpt(g, rr, max_time, start)
        print("after 2opt", (datetime.datetime.now() - start).seconds)
        mmd = distance(tr, g.getPairMatrix(), max_time, start)
        print("after dist", (datetime.datetime.now() - start).seconds)
        if (mmd != -1):
            rd = mmd
        if (rd < d):
            d = rd
            r = tr
    print(d)
    # print(r)
    fp = open(params[1], 'w')
    fp.write(str(d) + "\n")
    for city in r:
        fp.write(str(city) + " ")
    fp.write(str(r[0]))
    print((datetime.datetime.now() - start).seconds)






if __name__ == "__main__":
    main()

