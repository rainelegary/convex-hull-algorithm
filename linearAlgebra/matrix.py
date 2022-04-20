from linearAlgebra.vector import Vector


class Matrix:
	def __init__(self, mat):
		self.mat = mat


	def multMat(self, matA, matB):
		tableM = transpose(matB)
		return [[dotProduct(rowA, rowM) for rowM in tableM] for rowA in matA]


	def multVec(self, vector):
		return Vector([])


	def determinant(self):
		if len(mat) == 2: return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
		det = 0
		for elN in range(len(mat[0])):
			num = mat[0][elN]*cofactor(mat, 0, elN)
			det += num
		return det


	def isInvertible(self):
		return len(mat) == len(mat[0]) and determinant(mat) != 0


	def cofactor(self, i, j):
		matCopy = list(mat)
		multiplier = pow(-1, i + j)
		ijMat = []
		for rowN in range(len(matCopy)): 
			if rowN != i:
				matCopy[rowN] = removeAtIndex(matCopy[rowN], j)
				ijMat.append(matCopy[rowN])
		ijMinor = determinant(ijMat)
		return multiplier*ijMinor
			

	def transpose(self):
		self.mat = [getCol(matrix, col) for col in range(len(matrix[0]))]

	
	@staticmethod
	def getTranspose(matrix):
		mat = Matrix(matrix.mat)
		mat.transpose()
		return mat


	def getInverse(self):
		if not MatrixOperations.isInvertible(mat):
			sys.exit("Matrix is not invertible")
		size = len(mat)
		echelonMat = combineMatLeftRight(mat, identityMatrix(size))
		echelonMat = rEchelon(echelonMat)
		invMat = splitMatLeftRight(echelonMat, size)[1]
		return invMat

	@staticmethod
	def getRow(matrix, n):
		return table[n]


	@staticmethod
	def getCol(martix, n):
		values = [table[row][n] for row in range(len(table))]
		return values


	@staticmethod
	def identityMatrix(dimensions: int):
		return [[(1 if elN == row else 0) for elN in range(dimensions)] for row in range(dimensions)]


	@staticmethod
	def combineMatLeftRight(matA, matB):
		for rowN in range(len(matA)):
			for elN in matB[rowN]: 
				matA[rowN].append(elN)
		return matA


	@staticmethod
	def combineMatTopBottom(matA, matB):
		for row in matB: 
			matA.append(row)
		return matA


	@staticmethod
	def splitMatLeftRight(mat, index):
		matL = [mat[rowN][0:index] for rowN in range(len(mat))]
		matR = [mat[rowN][index:len(mat[0])] for rowN in range(len(mat))]
		return (matL, matR)


	@staticmethod
	def splitMatTopBottom(mat, index):
		matT = [mat[rowN] for rowN in range(0, index)]
		matB = [mat[rowN] for rowN in range(index, len(mat))]
		return (matT, matB)