

from linearAlgebra.matrix import Matrix


class RowEchelon:

	def __init__(self):
		pass


	def compute(self, mat):
		for row in range(mat.rowCount):
			mat = self.__nextRowOperations(mat, row)
		return mat


	def __nextRowOperations(self, mat, rowN):
		# swap to appropriate row
		rowToSwap = self.__needsRowSwap(mat, rowN)
		mat = self.__swapRows(mat, rowN, rowToSwap)

		# multiply row 
		colM = self.__firstNonZeroValue(mat[rowN])
		rowMult = 1/mat.mat[rowN][colM]
		mat = self.__multRow(mat, rowN, rowMult)

		# add row to other rows
		mat = self.__zeroColumn(mat, rowN, colM)

		return mat


	def __needsRowSwap(self, mat, rowN):
		for colN in range(rowN, mat.colCount):
			colList = mat.getCol(colN)
			for rowM in range(rowN, mat.rowCount):
				if colList[rowM] != 0: return rowM
		raise Exception("couldn't find a row to swap in row-echelon")


	def __zeroColumn(self, mat, rowN, colN):
		for rowM in range(mat.rowCount):
			if rowM != rowN:
				multiplier = mat.mat[rowM][colN]/mat.mat[rowN][colN]
				for colM in range(mat.colCount): 
					mat.mat[rowM][colM] -= mat.mat[rowN][colM] * multiplier
		return Matrix(mat.mat)


	def __swapRows(self, mat, rowN, rowM):
		rowC = mat.mat[rowN]
		mat.mat[rowN] = mat.mat[rowM]
		mat.mat[rowM] = rowC
		return Matrix(mat.mat)


	def __multRow(self, mat, rowN, multiplier):
		for elN in range(mat.colCount): 
			mat.mat[rowN][elN] *= multiplier
		return Matrix(mat.mat)


	def __addRow(self, mat, baseRow, addedRow):
		for elN in range(len(mat[0])):
			mat.mat[baseRow][elN] += mat[addedRow][elN]
		return Matrix(mat.mat)

	
	def __firstNonZeroValue(self, listL):
		for elN in range(len(listL)):
			if listL[elN] != 0:
				return elN
		raise Exception("No non-zero value found in the process of executing row-echelon")