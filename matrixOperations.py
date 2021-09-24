import sys

def matInverse(mat):
	if not isInvertible(mat):
		sys.exit("Matrix is not invertible")
	size = len(mat)
	echelonMat = combineMatLeftRight(mat, identityMatrix(size))
	echelonMat = rowEchelon(echelonMat)
	invMat = splitMatLeftRight(echelonMat, size)[1]
	return invMat


def rowEchelon(mat):
	for rowN in range(len(mat)):
		mat = nextRowOperations(mat, rowN)
	return mat


def nextRowOperations(mat, rowN):
	# swap to appropriate row
	rowToSwap = needsRowSwap(mat, rowN)
	mat = swapRows(mat, rowN, rowToSwap)

	# multiply row 
	colN = findFirstInList(mat[rowN], 0, avoid=True)
	rowMult = 1/mat[rowN][colN]
	mat = multRow(mat, rowN, rowMult)

	# add row to other rows
	mat = zeroColumn(mat, rowN, colN)

	return mat


def needsRowSwap(mat, rowN):
	for colN in range(rowN, len(mat[0])):
		colList = jColExtract(mat, colN)
		for rowM in range(rowN, len(mat)):
			if colList[rowM] != 0: return rowM


def zeroColumn(mat, rowN, colN):
	for rowM in range(len(mat)):
		if rowM != rowN:
			multiplier = mat[rowM][colN]/mat[rowN][colN]
			for colM in range(len(mat[0])): mat[rowM][colM] -= mat[rowN][colM] * multiplier
	return mat


def isInvertible(mat):
	if len(mat) != len(mat[0]) or determinant(mat) == 0: return False
	else: return True
	

def determinant(mat):
	if len(mat) == 2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
	det = 0
	for elN in range(len(mat[0])):
		num = mat[0][elN]*cofactor(mat, 0, elN)
		det += num
	return det


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
	return [matF]
		

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
		for elN in range(n): matI[row].append(0)
		matI[row][row] = 1
	return matI


def findFirstInList(listL, item, avoid=False):
	for elN in range(len(listL)):
		if listL[elN] == item and not avoid or listL[elN] != item and avoid: return elN
	return None


def countInList(listL, item):
	count = 0
	for el in listL:
		if el == item: count += 1
	return count


def removeAtIndex(listL, index):
	newList = []
	for elN in range(len(listL)):
		if elN != index: newList.append(listL[elN])
	return newList


