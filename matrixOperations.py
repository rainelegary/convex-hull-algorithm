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
	matF = []
	tableM = transpose(matB)

	matF = [[dotProduct(rowA, rowM) for rowM in tableM] for rowA in matA]
	return matF


def determinant(mat):
	if len(mat) == 2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
	det = 0
	for elN in range(len(mat[0])):
		num = mat[0][elN]*cofactor(mat, 0, elN)
		det += num
	return det


def isInvertible(mat):
	if len(mat) != len(mat[0]) or determinant(mat) == 0: return False
	else: return True


def cofactor(mat, i, j):
	matCopy = list(mat)
	mult = pow(-1, i + j)
	ijMat = []
	for rowN in range(len(matCopy)): 
		if rowN != i:
			matCopy[rowN] = removeAtIndex(matCopy[rowN], j)
			ijMat.append(matCopy[rowN])
	ijMinor = determinant(ijMat)
	return mult*ijMinor
		

def transpose(matrix):
	return [jColExtract(matrix, col) for col in range(len(matrix[0]))]


def dotProduct(u, v):
	sum = 0
	for el in range(len(u)): sum += u[el] * v[el]
	return sum

	
def identityMatrix(n):
	matI = []
	for row in range(n):
		matI.append([])
		for elN in range(n): matI[row].append(0)
		matI[row][row] = 1
	return matI


def flipVector(vector):
	for componentN in range(len(vector)): vector[componentN] *= -1
	return vector 


def sumVectors(vectorList):
	return [sum(vector[component] for vector in vectorList) for component in range(len(vectorList[0]))]


def subtractVectors(v1, v2):
	v2 = flipVector(v2)
	return sumVectors([v1, v2])


def unitVec(vector):
	length = vectorLength(vector)
	return multVector(vector, 1/length)


def multVector(vector, multiplier):
	return [vector[comp]*multiplier for comp in vector]


def vectorLength(vector):
	return pow(sum(comp*comp for comp in vector), 1/2)


def tinyVector(vector):
	for compN in range(len(vector)):
		vector[compN] *= 1/1000000
	return vector


# print(subtractVectors(identityMatrix(2)[0], identityMatrix(2)[1]))
# print(matMul([[1, 0], [0, 1]], [[1], [1]]))

