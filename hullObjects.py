from matrixOperations import sumVectors, subtractVectors, matInverse, transpose, flipVector, dotProduct, matMul, unitVec, vecToList
from copy import deepcopy
from random import random
import math

class PointCluster:
	def __init__(self, *args):
		self.points = []


class Simplex:
    def __init__(self, parent, vertices):
        self.parent = parent
        self.vertices = vertices
        # self.newestVertex = -1 # None?
        self.faces = self.__generateFaces()
        self.simplexChildren = []


    def calculateFace(self, vertexToRemove):
        # calculate direction of missing vertex from the plane
        # - find scalar form of plane
        # - each directional component of the vector will be a constant from the plane's scalar form
        # if the directon is facing the missing point, flip the direction
        oldVertex = self.vertices[vertexToRemove]
        simplexFace = SimplexFace(self, vertexToRemove)
        somePointOnFace = simplexFace.vertices[0]
        plane = simplexFace.plane
        dirVec = plane.dirVec

        samplePointA = Point(sumVectors([dirVec, somePointOnFace.location]))
        samplePointB = Point(sumVectors([flipVector(dirVec), somePointOnFace.location]))
        if oldVertex.distanceFromPoint(samplePointA) < oldVertex.distanceFromPoint(samplePointB):
            simplexFace.plane.dirVec = flipVector(dirVec)
            simplexFace.plane.quantity *= -1

        return simplexFace


    def checkCluster(self, cluster: PointCluster):
        for point in cluster.points:
            relativeLocation = point.locationRelativeToSimplex(self.faces, point.location)


    def __generateFaces(self):
        return [self.calculateFace(vertexN) for vertexN in range(len(self.vertices))]


    # def __generateFaces(self):
    #     return [SimplexFace(self, vertexN) for vertexN in range(len(self.vertices))]



class SimplexFace:
    def __init__(self, simplex, vertexToRemove):
        self.simplexParent = simplex
        self.vertices = self.initializeVertices(simplex, vertexToRemove)
        self.plane = self.calculatePlane()
        self.eligiblePoints = PointCluster()
        self.simplexChild = None


    def initializeVertices(self, simplex, vertexToRemove):
        vertices = deepcopy(simplex.vertices)
        vertices.pop(vertexToRemove)
        return vertices


    def calculatePlane(self):
        points = self.vertices
        vectorMat = [subtractVectors(points[0].location, points[i].location) for i in range(1, len(points))]
        vectorMat.append([random() for i in range(len(points[0].location))])

        dotProdVec = transpose([[0] * (len(points) - 1) + [1]])

        constantsVec = matMul(matInverse(vectorMat), dotProdVec)
        constants = unitVec(vecToList(constantsVec))

        quantity = dotProduct(constants, points[0].location)
        
        plane = Plane(constants, quantity)
        return plane


class Plane:
    def __init__(self, dirVec, quantity):
        self.dirVec = dirVec
        self.quantity = quantity


class Point:
    def __init__(self, location):
        self.location = location
        self.eligibleFaces = []


    def distanceFromPoint(self, otherPoint):
        return math.sqrt(sum(pow(self.location[i]-otherPoint.location[i], 2) for i in range(len(self.location))))

    
    def directionalDistance(self, dirVector):
        return sum(self.location[comp]*dirVector[comp] for comp in range(len(self.location)))


    def locationRelativeToSimplex(self, simplex: Simplex):
        relativeBounds = []
        for simplexFace in simplex.faces:
            plane = simplexFace.plane
            dirVec = plane.dirVec
            quantity = plane.quantity
            relativeBounds.append(dotProduct(dirVec, self.location) <= quantity)
        return relativeBounds