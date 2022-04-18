class Point:
    def __init__(self, location):
        self.location = location
        self.eligibleFaces = []


    def distanceFromPoint(self, otherPoint):
        return math.sqrt(sum(pow(self.location[i]-otherPoint.location[i], 2) for i in range(len(self.location))))

    
    def directionalDistance(self, dirVector):
        return sum(self.location[comp]*dirVector[comp] for comp in range(len(self.location)))


    def locationRelativeToSimplex(self, simplex: Simplex):
        return [simplexFace.containsPoint(self) for simplexFace in simplex.faces]   