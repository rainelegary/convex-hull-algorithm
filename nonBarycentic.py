from matrixOperations import dotProduct
from linearAlgebra import pointsToPlane, simpToPlane, simplexMissingVert


def relativeSimpLocation(simplexFaces, point):
	relativeBounds = []
	for simplexFace in simplexFaces:
		dVec = simplexFace[0], quantity = simplexFace[1]
		if dotProduct(dVec, point) <= quantity: relativeBounds.append(True)
		else: relativeBounds.append(False)
	return relativeBounds


def simplexFaces(simplex):
	return [simpToPlane(simplex, pointN) for pointN in range(len(simplex))]