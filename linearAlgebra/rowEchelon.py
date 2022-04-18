from deprecated.listOperations import ListOperations

class RowEchelon:
	lo = ListOperations()

	def __init__(self):
		pass

	def rEchelon(self, mat):
		for rowN in range(len(mat)):
			mat = self.__nextRowOperations(mat, rowN)
		return mat

	def __nextRowOperations(self, mat, rowN):
		# swap to appropriate row
		rowToSwap = self.__needsRowSwap(mat, rowN)
		mat = self.__swapRows(mat, rowN, rowToSwap)

		# multiply row 
		colN = self.lo.findFirstInList(mat[rowN], 0, avoid=True)
		rowMult = 1/mat[rowN][colN]
		mat = self.__multRow(mat, rowN, rowMult)

		# add row to other rows
		mat = self.__zeroColumn(mat, rowN, colN)

		return mat


	def __needsRowSwap(self, mat, rowN):
		for colN in range(rowN, len(mat[0])):
			colList = self.lo.getCol(mat, colN)
			for rowM in range(rowN, len(mat)):
				if colList[rowM] != 0: return rowM


	def __zeroColumn(self, mat, rowN, colN):
		for rowM in range(len(mat)):
			if rowM != rowN:
				multiplier = mat[rowM][colN]/mat[rowN][colN]
				for colM in range(len(mat[0])): mat[rowM][colM] -= mat[rowN][colM] * multiplier
		return mat


	def __swapRows(self, mat, rowN, rowM):
		rowC = mat[rowN]
		mat[rowN] = mat[rowM]
		mat[rowM] = rowC
		return mat


	def __multRow(self, mat, rowN, multiplier):
		for elN in range(len(mat[0])): mat[rowN][elN] *= multiplier
		return mat


	def __addRow(self, mat, baseRow, addedRow):
		for elN in range(len(mat[0])):
			mat[baseRow][elN] += mat[addedRow][elN]
		return mat