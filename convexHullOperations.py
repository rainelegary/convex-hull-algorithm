from matrixOperations import flipVector, identityMatrix, matMul, sumVectors, transpose, matInverse
from linearAlgebra import pointsToPlane, simpToPlane
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


def newDirection(simplex, missingVertex):
	return simpToPlane(simplex, missingVertex)[0]


def defineHullCenter(points):
	nPoints = len(points)
	components = [[] for dim in range(len(points[0]))]
	for point in points:
		for dim in range(len(point)): components[dim].append(point[dim])
	for component in components: component.sort()
	centerPoint = [component[nPoints // 2] for component in components]
	return centerPoint



print(newDirection(identityMatrix(3) + [[1, 2, 3]], 0))