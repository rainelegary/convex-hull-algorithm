from matrixOperations import flipVector, identityMatrix, matMul, sumVectors, transpose, matInverse
from linearAlgebra import pointsToPlane
import math


def selectFirstDirections(dims): 
	# https://math.stackexchange.com/questions/2533532/how-to-find-the-coordinates-of-an-n-dimensional-rectangular-simplex
	# https://en.wikipedia.org/wiki/Simplex
	a = (1 + math.sqrt(dims + 1))/dims
	translationConst = -(a+1)/(dims+1)

	simplex = [[0 + translationConst] * dims] * dims
	for dim in range(dims): simplex[dim][dim] = 1 + translationConst
	
	simplex.append([a + translationConst] * dims)
	return simplex


def newDirection(oldSimplex, missingVertex):
	# calculate direction of missing vertex from the plane
	# - find scalar form of plane
	# - each directional component of the vector will be a constant from the plane's scalar form
	# invert that direction; that's the direction this function should return
	oldVertex = oldSimplex[missingVertex]
	oldSimplex.pop(missingVertex)
	testPoint = oldSimplex[0]
	dVec = pointsToPlane(oldSimplex)[0]
	if pointDistance(sumVectors([dVec, testPoint]), oldVertex) < pointDistance(testPoint, oldVertex): dVec = flipVector(dVec)
	return dVec

	

def defineHullCenter(points): # prob won't actually need this function
	nPoints = len(points)
	components = [[] for dim in range(len(points[0]))]
	for point in points:
		for dim in range(len(point)): components[dim].append(point[dim])
	for component in components: component.sort()
	centerPoint = [component[nPoints // 2] for component in components]
	return centerPoint


def pointDistance(pointA, pointB):
	return math.sqrt(sum(pointA[i]*pointB[i] for i in range(len(pointA))))


print(newDirection(identityMatrix(3) + [[1, 2, 3]], 0))