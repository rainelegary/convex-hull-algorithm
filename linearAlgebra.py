from matrixOperations import dotProduct, matMul, subtractVectors, matInverse, transpose
from random import random

def pointsToPlane(points):

	vectorMat = [subtractVectors(points[0], points[i]) for i in range(1, len(points))]
	vectorMat.append([random() for i in range(len(points[0]))])
	dotProdVec = [[0] for i in range(len(points) - 1)]
	dotProdVec.append([1])
	constantsVec = matMul(matInverse(vectorMat), dotProdVec)
	constants = transpose(constantsVec)[0]
	quantity = dotProduct(constants, points[0])
	
	plane = (constants, quantity)
	return plane

	


