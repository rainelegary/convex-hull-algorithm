def calcInverse(mat):
	pass




def matMul(matA, matB):
	matF = []
	tableM = getTranspose(matB)
	for rowA in matA: 
		for rowM in tableM: matF.append(dotProduct(rowA, rowM))

	return matF
		

def getTranspose(matrix):
	T = [jColExtract(matrix, col) for col in range(len(matrix[0]))]
	return T


def dotProduct(u, v):
	sum = 0
	for el in range(len(u)): sum += u[el] * v[el]
	return sum


def jColExtract(table, j):
	values = [table[row][j] for row in range(len(table))]
	return values
	
