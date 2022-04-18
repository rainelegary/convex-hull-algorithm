class Simplex:
    def __init__(self, parent, vertices):
        self.parent = parent
        self.vertices = vertices
        # self.newestVertex = -1 # None?
        self.faces = self.__generateFaces()
        self.simplexChildren = []


    def checkCluster(self, cluster: PointCluster):
        for point in cluster.points:
            relativeLocation = point.locationRelativeToSimplex(self.faces, point.location)


    def __generateFaces(self):
        return [SimplexFace(self, vertexN) for vertexN in range(len(self.vertices))]