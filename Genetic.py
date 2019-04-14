#return list of tuples containing id, x, and y coordinates
import sys
import math
import random
import numpy as np
import datetime

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
        #creates dictionary of distances between all points
        self.pairMatrix = [[] for x in range(len(x_y))]
        for i in range(len(x_y)):
            for j in range(len(x_y)):
                self.pairMatrix[i].append(int(math.sqrt((x_y[i][1]-x_y[j][1])**2 + (x_y[i][2]-x_y[j][2])**2)))
    def getPairMatrix(self):
        return self.pairMatrix

    #calculates the distance of the route by adding up all the distances within the route
    #input: route, a list of distances

    def routeDistance(self, route):
        pathDistance = 0
        for city in range(len(route)):
            first_city = route[city]
            if city + 1 >= len(route):
                second_city = route[0]
            else:
                second_city = route[city + 1]
            pathDistance += self.pairMatrix[first_city - 1][second_city - 1]
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
        for i in range(popSize):
            population.append(self.createRoute())

        return population

    #checks the fitness for the population and returns a population and fitness list sorted by fitness
    def checkFitness(self, population):
        fitness = []
        for i in population:
            fitness.append([self.fitness(self.routeDistance(i)), population.index(i)])
        return sorted(fitness, reverse=True)

    def SelectionOfFittest(self, rankedPop, limit):
        selections = []
        sumFitness = 0
        for i in rankedPop:
            sumFitness += i[0]
        fitPro = []
        for i in rankedPop:
            fitPro.append(i[0]/float(sumFitness))
        #now that we have the fitness probabilities, we can select the necessary ones
        #selects the best routes to put in the next generation; elitism?
        for i in range(limit):
            selections.append(rankedPop[i][1])
        #fills the rest with random fitness 
        selections = selections + list(np.random.choice([route[1] for route in rankedPop], size=(len(rankedPop) - limit), p=fitPro))
        #print(selections)
        return selections

    def matingPool(self, population, selections):
        matingPool = []
        for a in range(len(selections)):
            index = selections[a]
            matingPool.append(population[index])
        return matingPool

    def crossOver(self, parent1, parent2):
        child = []
        childP1 = []
        childP2 = []
        
        gene1 = int(random.random() * len(parent1))
        gene2 = int(random.random() * len(parent1))
        
        startGene = min(gene1, gene2)
        endGene = max(gene2, gene2)

        for i in range(startGene, endGene):
            childP1.append(parent1[i])
            
        childP2 = [item for item in parent2 if item not in childP1]

        child = childP1 + childP2
        return child

    def breedPopulation(self, matingPool, elite_size):
        remaining = len(matingPool) - elite_size
        children = []
        #creates a pool of viable parents
        pool = random.sample(matingPool, len(matingPool))

        for i in range(elite_size):
            children.append(matingPool[i])

        for i in range(remaining):
            children.append(self.crossOver(pool[i], pool[len(matingPool) - i - 1]))
        return children


    def mutate(self,individual, mutation_prob):
        for i in range(len(individual)):
            if(random.random() < mutation_prob):
                swap = int(random.random() * len(individual))
                city1 = individual[i]
                individual[i] = individual[swap]
                individual[swap] = city1


            return individual

    def mutatePopulation(self,population, mutation_prob):
        mutatedPop = []

        for i in population:
            mutatedRoute = self.mutate(i, mutation_prob)
            mutatedPop.append(mutatedRoute)

        return mutatedPop

    def nextGeneration(self, generation, elite_size, mutation_prob):
        ranked_pop = self.checkFitness(generation)
        selections = self.SelectionOfFittest(ranked_pop, elite_size)
        children = self.breedPopulation(self.matingPool(generation, selections), elite_size)
        nextGeneration = self.mutatePopulation(children, mutation_prob)
        return nextGeneration

    def geneticAlgorithm(self, pop_size, elite_size, mutation_prob):
        pop = self.createPopulation(pop_size)
        print("Initial distance: " + str(1/self.checkFitness(pop)[0][0]))
        start = datetime.datetime.now()

        while (datetime.datetime.now() - start).seconds < self.maxTime - 2:
            pop = self.nextGeneration(pop, elite_size, mutation_prob)

        print("Final distance: " + str(1 / self.checkFitness(pop)[0][0]))
        best_route_i = self.checkFitness(pop)[0][1]
        print(1/self.checkFitness(pop)[0][0])
        bestRoute = pop[best_route_i]
        return 1/self.checkFitness(pop)[0][0], bestRoute




def main():
    start = datetime.datetime.now()
    params = input()
    graph = Graph("example_test.txt", params[2])
    #print(graph.getPairMatrix())
    #print("\n")
    dist, route = graph.geneticAlgorithm(200, 15, 0.01)
    print(dist, "\n")
    print(route)
    print("\n")
    #print("[")
    '''for city in range(len(route)):
        if city + 1 >= len(route):
            print(graph.getPairMatrix()[route[city] - 1][route[0] - 1], " ")
        else:
            print(graph.getPairMatrix()[route[city] - 1][route[city + 1] - 1], " ")
    print("]")'''
    fp = open(params[1], "w")
    fp.write(str(dist))
    fp.write("\n")
    for city in route:
        fp.write(str(city)+" ")
    fp.write(str(route[0]))
    print((datetime.datetime.now() - start).seconds)



if __name__ == "__main__":
    main()


