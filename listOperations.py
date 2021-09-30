
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


def listToVec(aList):
	return [[comp] for comp in aList]


def vecToList(vec):
	return [vec[compN][0] for compN in range(len(vec))]


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