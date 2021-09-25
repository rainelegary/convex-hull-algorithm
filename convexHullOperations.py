from matrixOperations import matMul, transpose, matInverse


def selectFirstDirections(dims): 
	# https://math.stackexchange.com/questions/2533532/how-to-find-the-coordinates-of-an-n-dimensional-rectangular-simplex
	# https://en.wikipedia.org/wiki/Simplex
	pass


def newDirection(oldSimplex, missingVertex):
	# calculate direction of missing vertex from the plane
	# - find scalar form of plane
	# - each directional component of the vector will be a constant from the plane's scalar form
	# invert that direction; that's the direction this function should return
	oldSimplex.pop(missingVertex)
	



def defineHullCenter(points): # prob won't actually need this function
	nPoints = len(points)
	components = [[] for dim in range(len(points[0]))]
	for point in points:
		for dim in range(len(point)): components[dim].append(point[dim])
	for component in components: component.sort()
	centerPoint = [component[nPoints // 2] for component in components]
	return centerPoint


