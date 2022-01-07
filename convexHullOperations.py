from matrixOperations import flipVector, identityMatrix, matMul, sumVectors, transpose, matInverse
import math
from random import uniform

def generatePoints(dimensions, numPoints):
	points = []
	for dim in range(dimensions): 
		for pointN in range(numPoints):
			pointFound = False
			while not pointFound:
				point = [uniform() for dim in range(dimensions)]
				if sum([c*c for c in point]) <= 1:
					points.append(point)
					pointFound=True
	return points


def firstSimplex(dims, points):
	vertices = []
	directions = selectFirstDirections(dims)
	for direction in directions:
		vertex = findFarthestPoint(points, direction)
		vertices.append(vertex)
	return vertices
		

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
	return simplexToPlane(simplex, missingVertex)[0]


def defineHullCenter(points):
	nPoints = len(points)
	components = [[] for dim in range(len(points[0]))]
	for point in points:
		for dim in range(len(point)): components[dim].append(point[dim])
	for component in components: component.sort()
	centerPoint = [component[nPoints // 2] for component in components]
	return centerPoint


def findFarthestPoint(points, dirVec):
	greatestDistance = 0
	farthestPoint = [0 for i in range(len(dirVec))]
	for point in points:
		distance = directionalDistance(dirVec, point)
		if distance > greatestDistance:
			greatestDistance = distance
			farthestPoint = point
	return farthestPoint




print(newDirection(identityMatrix(3) + [[1, 2, 3]], 0))