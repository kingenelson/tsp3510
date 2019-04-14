from Graph import Graph
from twoOpt import twoOpt
from twoOpt import distance
import random
import copy
import datetime
g = Graph("example_test.txt")
pm = g.getPairMatrix()
ir = list(range(1, len(pm)))
r = twoOpt(g, ir)
d = distance(r, g.getPairMatrix())

start = datetime.datetime.now()
while (datetime.datetime.now() - start).seconds < 180:
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

