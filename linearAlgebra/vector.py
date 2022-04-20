from geometricObjects.point import Point


class Vector:
	def __init__(self, vec):
		self.vec = vec
		self.dims = len(vec)

	@staticmethod
	def dotProduct(u, v):
		return sum(u.vec[el]*v.vec[el] for el in range(len(u.vec)))


	@staticmethod
	def flipped(vector):
		return Vector([-vector.vec[i] for i in range(vector.dims)])


	def flip(self):
		self.vec = [-self.vec[i] for i in range(self.dims)]


	@staticmethod
	def sumVectors(vectorList):
		vectorSize = len(vectorList[0].vec)
		return [sum(v.vec[i] for v in vectorList) for i in range(vectorSize)]


	@staticmethod
	def subtractVectors(v1, v2):
		return Vector.sumVectors([v1, Vector.flipped(v2)])


	@staticmethod
	def asUnitVec(vector):
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


	def asPoint(self):
		return Point(self.vec)

