from geometricObjects.simplex import Simplex
from matrixOperations import sumVectors, subtractVectors, matInverse, transpose, flipVector, dotProduct, matMul, unitVec, vecToList
from random import random
import math


class ConvexHull:
    def __init__(self, pointCluster):
        self.pointCluster = pointCluster
        self.dims = pointCluster.dims


    def firstSimplex(self):
        vertices = []
        directions = self.selectFirstDirections()
        for direction in directions:
            vertex = self.pointCluster.findFarthestPoint(direction)
            vertices.append(vertex)
        return Simplex(vertices)


    def selectFirstDirections(self): 
        dims = self.dims
        # https://math.stackexchange.com/questions/2533532/how-to-find-the-coordinates-of-an-n-dimensional-rectangular-simplex
        # https://en.wikipedia.org/wiki/Simplex
        a = (1 + math.sqrt(dims + 1))/dims
        translationConst = -(a+1)/(dims+1)

        directionVectors = [[0 + translationConst] * dims] * dims
        for dim in range(dims): 
            directionVectors[dim][dim] = 1 + translationConst
        
        directionVectors.append([a + translationConst] * dims)
        return directionVectors


    def defineHullCenter(points):
        nPoints = len(points)
        components = [[] for dim in range(len(points[0]))]
        for point in points:
            for dim in range(len(point)): components[dim].append(point[dim])
        for component in components: 
            component.sort()
        centerPoint = [component[nPoints // 2] for component in components]
        return centerPoint








    




