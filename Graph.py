class Graph:
    """docstring for Graph"""
    def __init__(self, points):
        # get points in from of [(ID, (X, Y)), ...]

        for i in range(0, len(points)):
            for j in range(0, len(points)):
                self.pairMatrix[i][j] = int(round(sqrt(int(round(points[i][1][0] - points[j][1][0]))^2 + int(round(points[i][1][1] - points[j][1][1]))^2)))

    def getPairMatrix(self):
        return self.pairMatrix
