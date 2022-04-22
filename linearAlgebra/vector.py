from geometricObjects.point import Point
import copy


class Vector:
	def __init__(self, vec):
		self.vec = copy.deepcopy(vec)
		self.dims = len(vec)


	def asPoint(self):
		return Point(self.vec)


	def getFlipped(self):
		return Vector([-comp for comp in self.vec])

	
	def getLength(self):
		return pow(sum([comp*comp for comp in self.vec]), 1/2)


	def asUnitVec(self):
		return self.scaleVector(1/self.getLength())


	def scaleVector(self, multiplier):
		return Vector([comp*multiplier for comp in self.vec])


	@staticmethod
	def dotProduct(u, v):
		return sum(u.vec[comp]*v.vec[comp] for comp in range(u.dims))


	@staticmethod
	def listDotProduct(u, v):
		return sum(u[comp]*v[comp] for comp in range(u.dims))


	@staticmethod
	def sumVectors(vectorList):
		vectorSize = vectorList[0].dims
		return Vector([sum(v.vec[comp] for v in vectorList) for comp in range(vectorSize)])


	@staticmethod
	def subtractVectors(v1, v2):
		return Vector.sumVectors([v1, Vector.getFlipped(v2)])


	@staticmethod
	def listToVec(aList):
		return [[comp] for comp in aList]


	@staticmethod
	def vecToList(vec):
		return [vec[compN][0] for compN in range(len(vec))]




