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

