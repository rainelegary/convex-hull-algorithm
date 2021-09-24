


def selectDirections(dims): 
	# https://math.stackexchange.com/questions/2533532/how-to-find-the-coordinates-of-an-n-dimensional-rectangular-simplex
	# https://en.wikipedia.org/wiki/Simplex
	pass


def defineHullCenter(points):
	nPoints = len(points)
	components = [[] for dim in range(len(points[0]))]
	for point in points:
		for dim in range(len(point)): components[dim].append(point[dim])
	for component in components: component.sort()
	centerPoint = [component[nPoints // 2] for component in components]
	return centerPoint


