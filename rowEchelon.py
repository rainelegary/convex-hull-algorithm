from listOperations import jColExtract, findFirstInList

def rEchelon(mat):
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