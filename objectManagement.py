from linearAlgebra import simpToPlane
from nonBarycentic import relativeSimpLocation
from convexHullOperations import firstSimplex
from randomPoints import generatePoints
from convexHullLab import HullSettings


class ObjectInterface:
	def __init__(self, dimensions):
		self.__hullSettings = HullSettings(3, 1000)
		self.__dims = self.__hullSettings.dimensions
		self.__starterPoints = StarterPoints()
		self.__simplexTree = SimplexTree()
		self.__objRef = self.setupObjectReferences()


	def setupObjectReferences(self):
		objectReferences = {}
		objectReferences['point'] = {}
		objectReferences['simplex'] = {}
		objectReferences['face'] = {}
		self.__objRef = objectReferences


	def getPoint(self, pointName):
		return self.__objRef['point'][pointName]


	def getSimplex(self, simplexName):
		return self.__objRef['simplex'][simplexName]


	def getFace(self, faceName):
		return self.__objRef['face'][faceName]


	def __firstGeneration(self):
		mainSimplex = Simplex("simplex_l0_0", firstSimplex(self.__dims, self.__starterPoints.points))


	
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
		
	

class PointList:
	def __init__(self):
		self.points = []


class StarterPoints(PointList):
	def __init__(self):
		self.points = self.pointGeneration()


	def pointGeneration(self):
		return generatePoints(HullSettings.numPoints, HullSettings.dimensions)


class Point:
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.eligibleFaces = {}


class SimplexTree:
	def __init__(self):
		self.tree = {'layer0': {}, 'layer1': {}, 'layer2': {}}


class Simplex:
	def __init__(self, name, parent, vertices):
		self.name = name
		self.parent = parent
		self.vertices = vertices
		self.newestVertex = -1
		self.faces = self.__generateFaces()
		self.children = []


	def setChildren(self, children):
		self.children = children


	def checkCluster(self, cluster):
		for point in cluster.points.values():
			relativeLocation = relativeSimpLocation(self.faces, point.location)


	def __generateFaces(self):
		return [simpToPlane(self.vertices, vertexN) for vertexN in range(len(self.vertices))]


class SimplexFace:
	def __init__(self, name):
		self.name = name
		self.vertexNames = []
		self.plane = None
		self.eligiblePoints = PointList()
		self.simplexChild = None









