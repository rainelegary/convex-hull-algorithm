from dataclasses import dataclass
from linearAlgebra import simpToPlane
from nonBarycentic import relativeSimpLocation
from convexHullOperations import selectFirstDirections


@dataclass
class ClusterList:
	name: str
	clusters: dict = {}

	def addCluster(self, cluster):
		self.clusters[cluster.name] = cluster
	
	def removeCluster(self, clusterName):
		del self.clusters[clusterName]


@dataclass
class PointCluster:
	def __init__(self, name: str, dirVec: list, points: dict):
		self.name = name
		self.dirVec = dirVec
		self.points = points

	def addPoint(self, point):
		self.points[point.name] = point

	def removePoint(self, pointName):
		del self.points[pointName]


@dataclass
class Point:
	name: str
	location: list


@dataclass
class SimplexList:
	name: str
	simplices: dict = {}

	def addSimplex(self, simplex):
		self.simplices[simplex.name] = simplex

	def removeSimplex(self, simplexName):
		del self.simplices[simplexName]



class Simplex:
	def __init__(self, name: str, clusters: dict, vertices: list):
		self.name = name
		self.clusters = clusters
		self.vertices = vertices
		self.faces = self.__generateFaces()


	def addCluster(self, cluster):
		self.clusters.append(cluster)


	def clearAllPoints(self):
		for cluster in self.clusters: self.checkCluster(cluster)


	def checkCluster(self, cluster):
		for point in cluster.points.values():
			relativeLocation = relativeSimpLocation(self.faces, point.location)


	def __generateFaces(self):
		return [simpToPlane(self.vertices, vertexN) for vertexN in range(len(self.vertices))]












