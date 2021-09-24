from barycentric import *


def hullMainScript():
	simplex = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
	simpMat = simplexMatrix(simplex)
	point = [[0, 0.5001, 0.5, 0]]
	print(pointInside(simplex, point, simpMat))


if __name__ == '__main__':
	hullMainScript()