import random
from geometricObjects.plane import Plane
from geometricObjects.point import Point
from linearAlgebra.matrix import Matrix
from linearAlgebra.vector import Vector


class SimplexFace:
    def __init__(self, simplex, missingVertex):
        self.dims = simplex.dims
        self.missingVertex = missingVertex
        self.vertices = simplex.vertices
        self.vertices.remove(missingVertex)
        self.plane = self.initializePlane()
        self.dirVec = self.plane.coefficients


    def initializePlane(self):
        # linear algebra
        vectors = [vertex.asVector() for vertex in self.vertices]
        vectorMat = [Vector.subtractVectors(vectors[0], vectors[i]) for i in range(1, self.dims)]
        vectorMat.append([random() for i in range(self.dims)])
        dotProdVec = Vector([[0] * (self.dims - 1) + [1]])
        coefficients = Matrix.getInverse(vectorMat).multVec(dotProdVec).asUnitVec()
        quantity = Vector.dotProduct(coefficients, vectors[0])
        plane = Plane(coefficients, quantity)


        # orient plane away from old vertex
        testPoint = self.vertices[0]

        pointAlongVec = Point(Vector.sumVectors([plane.coefficients, testPoint.coords]))
        pointAgainstVec = Point(Vector.sumVectors([Vector.flipped(plane.coefficients), testPoint.coords]))

        if self.missingVertex.distanceFromPoint(pointAlongVec) < self.missingVertex.distanceFromPoint(pointAgainstVec):
            plane = plane.getFlipped()

        return plane


    def facesPoint(self, point):
        return Vector.dotProduct(self.plane.coefficients, point.coords.asVector()) <= self.plane.quantity