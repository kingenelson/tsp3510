#return list of tuples containing id, x, and y coordinates
import math
import random
class Graph:
    """docstring for Graph"""
    def __init__(self, fileName):
        # get points in from of [(ID, (X, Y)), ...]
        fp = open(fileName, 'r')
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


        # print (self.pairMatrix)
    def getPairMatrix(self):
        return self.pairMatrix





def main():
    graph = Graph("example_test.txt")

if __name__ == "__main__":
    main()


