#return list of tuples containing id, x, and y coordinates
import math
import random
import numpy as np
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

    #calculates the distance of the route by adding up all the distances within the route
    #input: route, a list of distances

    def routeDistance(self, route):
        pathDistance = 0
        for city in len(route):
            first_city = route[city]
            if city + 1 >= len(route):
                second_city = route[0]
            else:
                second_city = route[city + 1]
            pathDistance += self.pairMatrix[first_city][second_city]
        return pathDistance

    #checks the fitness of the individual; in this case, the individual's fitness is the smaller distance
    def fitness(self, pathDistance):
        return 1/float(pathDistance)

    def createRoute(self):
        route = random.sample(self.cities, len(self.cities))
        return route

    #creates population of routes 
    def createPopulation(self, popSize):
        population = []
        for i in range(len(popSize)):
            population.append(self.createRoute())

        return population

    #checks the fitness for the population and returns a population and fitness list sorted by fitness
    def checkFitness(self, population):
        fitness = []
        for i in population:
            fitness.append([self.fitness(i), i])
        return sorted(fitness, key=lambda fit: fit[0])

    def SelectionOfFittest(self, rankedPop, limit):
        selections = []
        sumFitness = 0
        for i in rankedPop:
            sumFitness += i[0]
        fitPro = []
        for i in rankedPop:
            fitPro.append(i/float(sumFitness))
        #now that we have the fitness probabilities, we can select the necessary ones
        #selects the best routes to put in the next generation; elitism?
        for i in range(limit):
            selections.append(rankedPop[i][0])

        selections = selections + np.random.choice([rankedPop[:][1]], size=(len(rankedPop) - limit), p=fitPro)








def main():
    graph = Graph("example_test.txt")

if __name__ == "__main__":
    main()


