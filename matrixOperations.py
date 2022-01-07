import sys
from listOperations import listToVec, vecToList, jColExtract, removeAtIndex, combineMatLeftRight, splitMatLeftRight
from rowEchelon import rEchelon

def matInverse(mat):
	if not isInvertible(mat):
		sys.exit("Matrix is not invertible")
	size = len(mat)
	echelonMat = combineMatLeftRight(mat, identityMatrix(size))
	echelonMat = rEchelon(echelonMat)
	invMat = splitMatLeftRight(echelonMat, size)[1]
	return invMat


def matMul(matA, matB):
	tableM = transpose(matB)
	return [[dotProduct(rowA, rowM) for rowM in tableM] for rowA in matA]


def determinant(mat):
	if len(mat) == 2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
	det = 0
	for elN in range(len(mat[0])):
		num = mat[0][elN]*cofactor(mat, 0, elN)
		det += num
	return det


def isInvertible(mat):
	return len(mat) == len(mat[0]) and determinant(mat) != 0


def cofactor(mat, i, j):
	matCopy = list(mat)
	multiplier = pow(-1, i + j)
	ijMat = []
	for rowN in range(len(matCopy)): 
		if rowN != i:
			matCopy[rowN] = removeAtIndex(matCopy[rowN], j)
			ijMat.append(matCopy[rowN])
	ijMinor = determinant(ijMat)
	return multiplier*ijMinor
		

def transpose(matrix):
	return [jColExtract(matrix, col) for col in range(len(matrix[0]))]


def dotProduct(u, v):
	return sum(u[el]*v[el] for el in range(len(u)))

	
def identityMatrix(dimensions: int):
	return [[(1 if elN == row else 0) for elN in range(dimensions)] for row in range(dimensions)]


def flipVector(vector):
	return [-vector[componentN] for componentN in range(len(vector))]


def sumVectors(vectorList):
	return [sum(vector[component] for vector in vectorList) for component in range(len(vectorList[0]))]


def subtractVectors(v1, v2):
	return sumVectors([v1, flipVector(v2)])


def unitVec(vector):
	return multVector(vector, 1/vectorLength(vector))


def multVector(vector, multiplier):
	return [vector[comp]*multiplier for comp in vector]


def vectorLength(vector):
	return pow(sum(comp*comp for comp in vector), 1/2)

