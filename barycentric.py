from matrixOperations import *


def pointInside(simplex, point, simplexMat):
	lambdaVec = barycentric(simplex, point, simplexMat)
	isInside = True
	for lam in lambdaVec[0]:
		if lam < 0: isInside = False
	return isInside


def simplexMatrix(simplex):
	dimensions = len(simplex) - 1
	matT = [[simplex[j][i] - simplex[-1][i] for j in range(len(simplex) - 1)] for i in range(dimensions)]
	simpMat = matInverse(matT)
	return simpMat


def barycentric(simplex, point, simplexMat):
	# source: https://en.wikipedia.org/wiki/Barycentric_coordinate_system 
	# section: Barycentric coordinates on Tetrahedra
	dimensions = len(point[0])
	multVec = transpose([[point[0][i] - simplex[-1][i] for i in range(dimensions)]])
	lambdaVec = matMul(simplexMat, multVec)
	finalLambda = 1 - sum(lambdaVec[0])
	lambdaVec[0].append(finalLambda)
	return lambdaVec 


def calcDistance(dirVector, point):
	distance = sum(point[0][comp]*dirVector[0][comp] for comp in range(len(point[0])))
	return distance


def unitVec(vector):
	length = pow(sum(comp*comp for comp in vector[0]), 1/2)
	unitVec = [[comp/length for comp in vector[0]]]
	return unitVec