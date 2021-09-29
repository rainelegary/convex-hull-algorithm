from matrixOperations import dotProduct, identityMatrix, matMul, sumVectors, subtractVectors, matInverse, transpose, flipVector
from random import random
import math

def pointsToPlane(points):

	vectorMat = [subtractVectors(points[0], points[i]) for i in range(1, len(points))]
	vectorMat.append([random() for i in range(len(points[0]))])

	dotProdVec = transpose([[0] * (len(points) - 1) + [1]])

	constantsVec = matMul(matInverse(vectorMat), dotProdVec)
	constants = transpose(constantsVec)[0]
	quantity = dotProduct(constants, points[0])
	
	plane = (constants, quantity)
	return plane


def unitVec(vector):
	length = pow(sum(comp*comp for comp in vector[0]), 1/2)
	unitVec = [[comp/length for comp in vector[0]]]
	return unitVec


def pointDistance(pointA, pointB):
	return math.sqrt(sum(pow(pointA[i]-pointB[i], 2) for i in range(len(pointA))))


def directionalDistance(dirVector, point):
	distance = sum(point[comp]*dirVector[comp] for comp in range(len(point)))
	return distance


def simpToPlane(simplex, missingVertex):
	# calculate direction of missing vertex from the plane
	# - find scalar form of plane
	# - each directional component of the vector will be a constant from the plane's scalar form
	# if the directon is facing the missing point, flip the direction
	oldVertex = simplex[missingVertex]
	simplexFace = simplexMissingVert(simplex, missingVertex)
	testPoint = simplexFace[0]
	plane = pointsToPlane(simplexFace)
	dVec = plane[0], quantity = plane[1]
	if pointDistance(sumVectors([tinyVector(dVec), testPoint]), oldVertex) < pointDistance(testPoint, oldVertex): 
		dVec = flipVector(dVec)
		quantity *= -1

	return (dVec, quantity)


def simplexMissingVert(simplex, vertIndex):
	simplex.pop(vertIndex)
	return simplex


def tinyVector(vector):
	for compN in range(len(vector)):
		vector[compN] *= 1/1000000
	return vector


# print(pointsToPlane([[4, 0, 3], [0, 0, 1], [10, 0, 5]]))
# print(pointsToPlane(identityMatrix(3)))


	


