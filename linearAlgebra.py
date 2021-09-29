from matrixOperations import dotProduct, identityMatrix, matMul, subtractVectors, matInverse, transpose
from random import random

def pointsToPlane(points):

	vectorMat = [subtractVectors(points[0], points[i]) for i in range(1, len(points))]
	vectorMat.append([random() for i in range(len(points[0]))])

	dotProdVec = transpose([[0] * (len(points) - 1) + [1]])

	constantsVec = matMul(matInverse(vectorMat), dotProdVec)
	constants = transpose(constantsVec)[0]
	quantity = dotProduct(constants, points[0])
	
	plane = (constants, quantity)
	return plane


# print(pointsToPlane([[4, 0, 3], [0, 0, 1], [10, 0, 5]]))
# print(pointsToPlane(identityMatrix(3)))


	


