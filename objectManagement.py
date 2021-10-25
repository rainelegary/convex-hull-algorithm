from linearAlgebra import simpToPlane
from nonBarycentic import relativeSimpLocation
from convexHullOperations import selectFirstDirections


class ObjectInterface:
	def __init__(self, name, dimensions):
		self.name = name
		self.dimensions = dimensions
		self.points = PointList()
		self.simplexTree = SimplexTree()
		self.objectReferences = self.setupObjectReferences()


	def setupObjectReferences(self):
		objectReferences = {}
		objectReferences['points'] = {}
		objectReferences['simplices'] = {}
		objectReferences['simplex faces'] = {}
		self.objectReferences = objectReferences


	def firstGeneration(self):
		pass

	
	def newGeneration(self):
		pass


	def boundaryChecks(self):
		pass

	
	def pointUpdates(self):
		pass


	def objectManagerMain(self):
		# create first simplex
		mainSimplex = Simplex("simplex0",)
	

class PointList:
	def __init__(self):
		self.points = []


class Point:
	def __init__(self, name, location):
		self.name = name
		self.location = location
		self.eligibleFaces = {}


class SimplexTree:
	def __init__(self):
		self.tree = {'root': {}, 'layer 1': {}, 'layer 2': {}}


class Simplex:
	def __init__(self, name: str, vertices: list):
		self.name = name
		self.vertices = vertices
		self.faces = self.__generateFaces()


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
		self.eligiblePoints = {}
		self.simplexChild = None









