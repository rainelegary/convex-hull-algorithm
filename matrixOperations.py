import sys

def calcInverse(mat):
	if not isInvertible(mat):
		sys.exit("Matrix is not invertible")
	size = len(mat)
	echelonMat = combineMatLeftRight(mat, identityMatrix(size))
	echelonMat = rowEchelon(echelonMat)
	invMat = splitMatLeftRight(echelonMat, size)
	return invMat


def rowEchelon(mat):
	pass


def nextRowOperations(mat, rowN):
	pass


def needsRowSwap(mat, rowN):
	if mat[rowN][rowN] != 0:
		return rowN
	


	


def isInvertible(mat):
	if len(mat) != len(mat[0]) or determinant(mat) == 0: return False
	else: return True
	

def determinant(mat):
	if len(mat) == 2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
	det = 0
	for elN in mat[0]:
		num = mat[0][elN]*cofactor(mat, 0, elN)
		det += num
	return num


def cofactor(mat, i, j):
	mult = pow(-1, i + j)
	ijMat = []
	for rowN in range(len(mat)): 
		if rowN != i: ijMat.append(mat[rowN].pop(j))
	ijMinor = determinant(ijMat)
	return mult*ijMinor
	


def swapRows(mat, rowN, rowM):
	rowC = mat[rowN]
	mat[rowN] = mat[rowM]
	mat[rowM] = rowC
	return mat


def multRow(mat, rowN, multiplier):
	for elN in range(len(mat[0])): mat[rowN][elN] *= multiplier
	return mat


def addRow(mat, baseRow, addedRow):
	for elN in range(len(mat[0])):
		mat[baseRow][elN] += mat[addedRow][elN]
	return mat



def matMul(matA, matB):
	matF = []
	tableM = transpose(matB)
	for rowA in matA: 
		for rowM in tableM: matF.append(dotProduct(rowA, rowM))
	return matF
		

def transpose(matrix):
	return [jColExtract(matrix, col) for col in range(len(matrix[0]))]


def dotProduct(u, v):
	sum = 0
	for el in range(len(u)): sum += u[el] * v[el]
	return sum


def jColExtract(table, j):
	values = [table[row][j] for row in range(len(table))]
	return values


def combineMatLeftRight(matA, matB):
	for rowN in range(len(matA)):
		for elN in matB[rowN]: matA[rowN].append(elN)
	return matA


def combineMatTopBottom(matA, matB):
	for row in matB: matA.append(row)
	return matA


def splitMatLeftRight(mat, index):
	matL = [mat[rowN][0:index] for rowN in range(len(mat))]
	matR = [mat[rowN][index:len(mat[0])] for rowN in range(len(mat))]
	return (matL, matR)


def splitMatTopBottom(mat, index):
	matT = [mat[rowN] for rowN in range(0, index)]
	matB = [mat[rowN] for rowN in range(index, len(mat))]
	return (matT, matB)

	

def identityMatrix(n):
	matI = []
	for row in range(n):
		matI.append([])
		for elN in range(n): matI[row][elN] = 0
		matI[row][row] = 1
	return matI

