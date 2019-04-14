# Runs 2-opt on a graph
def twoOpt(graph):
    # Generate a random cycle and calcs its distance
    pm = graph.getPairMatrix()
    route = range(1, len(pm) + 1)
    d = distance(tour, pm)
    # for every i
    for i in range(0, len(route) - 1):
        # for every k
        for k in range(i, len(route)):
            newRoute = route[0:i] + route[i:k:-1] + route[k:]
            newd = distance(newRoute, pairMatrix)
            if (newd < d):
                d= newd
    return route

def distance(route, pairMatrix, start=0, end=len(tour)-1):
    dist = 0
    # for every node in tour - 1
    for i in range(start, end - 1):
        dist += pairMatrix[route[i]][route[i + 1]]
    return dist
