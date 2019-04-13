import sys
import math



def input():
    filename = str(sys.argv[1])
    output = str(sys.argv[2])
    max_time = int(sys.argv[3])
    return [filename, output, max_time]

class Graph:
    """docstring for Graph"""
    def __init__(self, fileName, maxTime):
        # get points in from of [(ID, (X, Y)), ...]
        fp = open(fileName, 'r')
        self.maxTime = maxTime
        x_y = []
        for line in fp:
            lines = line.split()
        #appends a new tuple with id, x, and y coordinates into list 
            x_y.append((int(float(lines[0])), int(float(lines[1])), int(float(lines[2]))))
        self.cities = [city[0] for city in x_y]
        print(x_y)
        #creates dictionary of distances between all points
        self.pairMatrix = [[] for x in range(len(x_y))]
        for i in range(len(x_y)):
            for j in range(len(x_y)):
                self.pairMatrix[i].append(int(math.sqrt((x_y[i][1]-x_y[j][1])**2 + (x_y[i][2]-x_y[j][2])**2)))

        print (self.pairMatrix)
    def getPairMatrix(self):
        return self.pairMatrix


def main():
    params = input()
    graph = Graph(params[0], params[2])
    #assume algorithm works here
    #then some defined output method



if __name__ == "__main__":
    main()
