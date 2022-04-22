from geometricObjects.simplexFace import SimplexFace


class Simplex:
    def __init__(self, parent, vertices):
        self.parent = parent
        self.vertices = vertices
        # self.newestVertex = None
        self.faces = self.__generateFaces()
        self.simplexChildren = []


    def checkCluster(self, cluster):
        for point in cluster.points:
            relativeLocation = point.locationRelativeToSimplex(self.faces, point.location)


    def __generateFaces(self):
        return [SimplexFace(self, vertex) for vertex in self.vertices]