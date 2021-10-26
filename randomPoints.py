from random import uniform

def generatePoints(numPoints, dimensions):
	points = []
	for dim in range(dimensions): 
		for pointN in range(numPoints):
			pointFound = False
			while not pointFound:
				point = [uniform() for dim in range(dimensions)]
				if sum([c*c for c in point]) <= 1:
					points.append(point)
					pointFound=True
	return points
