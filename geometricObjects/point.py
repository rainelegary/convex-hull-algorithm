import math

from linearAlgebra.vector import Vector

# updated
class Point:
    def __init__(self, coords):
        self.coords = coords
        self.dims = len(coords)


    def distanceFromPoint(self, otherPoint):
        return math.sqrt(sum(pow(self.coords[i]-otherPoint.coords[i], 2) for i in range(self.dims)))

    
    def directionalDistance(self, dirVector):
        return sum(self.coords[i]*dirVector[i] for i in range(self.dims))


    def locationRelativeToSimplex(self, simplex):
        return [not simplexFace.facesPoint(self) for simplexFace in simplex.faces]   

    
    def asVector(self):
        return Vector(self.coords)