from linearAlgebra.rowEchelon import RowEchelon
from linearAlgebra.vector import Vector
import copy


class Matrix:
	def __init__(self, mat):
		self.rowCount = len(mat)
		self.colCount = len(mat[0])
		self.mat = copy.deepcopy(mat)
		self.rows = copy.deepcopy(mat)
		self.cols = self.__initializeCols()
		self.cofactors = None
		self.determinant = None
		self.inverse = None

	
	def __initializeCols(self):
		columns = [[self.rows[row][col] for row in range(self.rowCount)] for col in range(self.colCount)]
		return columns

	
	def __initializeNoneCofactors(self):
		cofactors = [[None for col in range(self.colCount)] for row in range(self.rowCount)]
		return cofactors


	def multMatrix(self, matrix):
		if self.colCount != matrix.rowCount:
			raise Exception("Cannot multiply matrix: mismatched sizes")
		return Matrix([[Vector.listDotProduct(row, col) for col in matrix.cols] for row in self.rows])


	def multVector(self, vector):
		if self.colCount != vector.dims:
			raise Exception("Cannot multiply vector: mismatched sizes")
		return Vector([Vector.listDotProduct(row, Vector.vecToList(vector)) for row in self.rows])


	def getDeterminant(self):
		if self.rowCount != self.colCount:
			raise Exception("Cannot take determinant of a non-square matrix")

		if self.determinant != None:
			return self.determinant

		mat = self.mat 
		if self.rowCount == 2: 
			det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
			self.determinant = det
			return det

		det = 0
		for i in range(self.dims):
			num = mat[0][i]*self.getCofactor(mat, 0, i)
			det += num
		self.determinant = det
		return det


	def getCofactor(self, row, col):
		if self.cofactors == None:
			self.cofactors = self.__initializeNoneCofactors()

		if self.cofactors[row][col] != None:
			return self.cofactors[row][col]

		matCopy = copy.deepcopy(self.mat)
		multiplier = pow(-1, row + col)

		matCopy.pop(row)
		for rowN in range(len(matCopy)):
			matCopy[rowN].pop(col)
		
		rowColMatrix = Matrix(matCopy)
		rowColMinor = rowColMatrix.getDeterminant()

		cofactor = multiplier * rowColMinor
		self.cofactors[row][col] = cofactor
		return cofactor
			

	def getTranspose(self):
		return copy.deepcopy([self.getCol(col) for col in range(self.colCount)])


	def getInverse(self):
		if not self.getInvertible():
			raise Exception("Cannot invert an uninvertible matrix")
		size = self.rowCount
		rowEchelon = RowEchelon()
		rowEchelonMat = Matrix.combineMatLeftRight(self, Matrix.identityMatrix(size))
		rowEchelonMat = rowEchelon.compute(rowEchelonMat)
		invMat = Matrix.splitMatLeftRight(rowEchelonMat, size)["right"]
		return invMat


	def calculateCofactors(self):
		self.cofactors = [[self.getCofactor(row, col) for col in range(self.colCount)] for row in range(self.rowCount)]


	def getInvertible(self):
		invertible = self.rowCount == self.colCount and self.getDeterminant() != 0
		return invertible


	def getRow(self, row):
		return copy.deepcopy(self.rows[row])

	
	def getCol(self, col):
		return copy.deepcopy(self.cols[col])


	@staticmethod
	def identityMatrix(dims):
		return Matrix([[(1 if elN == row else 0) for elN in range(dims)] for row in range(dims)])


	@staticmethod
	def combineMatLeftRight(matA, matB):
		if matA.rowCount != matB.rowCount:
			raise Exception("Cannot combine matrices: mismatched size")
		
		matA = Matrix(matA.mat)
		matB = Matrix(matB.mat)
		matC = Matrix([matA.mat[row] + matB.mat[row] for row in range(matA.rowCount)])
		return matC


	@staticmethod
	def combineMatTopBottom(matA, matB):
		if matA.colCount != matB.colCount:
			raise Exception("Cannot combine matrices: mismatched size")

		matA = copy.deepcopy(matA)
		matB = copy.deepcopy(matB)
		matC = Matrix(matA.mat + matB.mat)
		return matC


	@staticmethod
	def splitMatLeftRight(matrix, index):
		if not 0 <= index <  matrix.colCount:
			raise Exception("Cannot split matrix: index out of bounds")
		
		matL = Matrix([matrix.mat[rowN][0:index] for rowN in range(matrix.rowCount)])
		matR = Matrix([matrix.mat[rowN][index:matrix.colCount] for rowN in range(matrix.rowCount)])
		return {"left": matL, "right": matR}


	@staticmethod
	def splitMatTopBottom(matrix, index):
		if not 0 <= index < matrix.rowCount:
			raise Exception("Cannot split matrix: index out of bounds")

		matT = Matrix([matrix.mat[rowN] for rowN in range(0, index)])
		matB = Matrix([matrix.mat[rowN] for rowN in range(index, matrix.rowCount)])
		return {"top": matT, "bottom": matB}