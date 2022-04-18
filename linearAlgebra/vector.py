class Vector:
	def __init__():
		pass

	@staticmethod
	def dotProduct(u, v):
		return sum(u[el]*v[el] for el in range(len(u)))

	@staticmethod
	def flipVector(vector):
		return [-vector[componentN] for componentN in range(len(vector))]


	@staticmethod
	def sumVectors(vectorList):
		return [sum(vector[component] for vector in vectorList) for component in range(len(vectorList[0]))]


	@staticmethod
	def subtractVectors(v1, v2):
		return sumVectors([v1, flipVector(v2)])


	@staticmethod
	def unitVec(vector):
		return multVector(vector, 1/vectorLength(vector))


	@staticmethod
	def multVector(vector, multiplier):
		return [vector[comp]*multiplier for comp in vector]


	@staticmethod
	def vectorLength(vector):
		return pow(sum(comp*comp for comp in vector), 1/2)


	@staticmethod
	def listToVec(aList):
		return [[comp] for comp in aList]


	@staticmethod
	def vecToList(vec):
		return [vec[compN][0] for compN in range(len(vec))]