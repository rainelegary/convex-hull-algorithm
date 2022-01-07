from convexHullOperations import firstSimplex
from convexHullLab import HullSettings


class ObjectInterface:
	def __init__(self):
		pass


	def run():
		pass


	def __firstGeneration(self):
		mainSimplex = Simplex(parent=None, vertices=firstSimplex(self.__dims, self.__starterPoints.points))

	
	def __newGeneration(self):
		# simplex parents and children
		pass


	def __boundaryChecks(self):
		# simplex face's point lists
		pass

	
	def __pointUpdates(self):
		pass


	def objectManagerMain(self):
		self.__firstGeneration()
		
	











