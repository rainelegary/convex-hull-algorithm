class SimplexFace:
    def __init__(self, simplex, vertexToRemove):
        self.simplexParent = simplex
        self.vertices = self.initializeVertices(simplex, vertexToRemove)
        self.oldVertex = simplex.vertices[vertexToRemove]
        self.plane = self.calculatePlane()
        self.eligiblePoints = PointCluster()
        self.simplexChild = None


    def initializeVertices(self, simplex, vertexToRemove):
        vertices = list(simplex.vertices)
        vertices.pop(vertexToRemove)
        return vertices


    def calculatePlane(self):
        # linear algebra
        points = self.vertices
        vectorMat = [subtractVectors(points[0].location, points[i].location) for i in range(1, len(points))]
        vectorMat.append([random() for i in range(len(points[0].location))])
        dotProdVec = transpose([[0] * (len(points) - 1) + [1]])
        constantsVec = matMul(matInverse(vectorMat), dotProdVec)
        constants = unitVec(vecToList(constantsVec))
        quantity = dotProduct(constants, points[0].location)
        plane = Plane(constants, quantity)


        # orient plane away from old vertex
        somePointOnFace = self.vertices[0]

        samplePointAlong = Point(sumVectors([plane.dirVec, somePointOnFace.location]))
        samplePointAgainst = Point(sumVectors([flipVector(plane.dirVec), somePointOnFace.location]))
        if self.oldVertex.distanceFromPoint(samplePointAlong) < self.oldVertex.distanceFromPoint(samplePointAgainst):
            plane.dirVec = flipVector(plane.dirVec)
            plane.quantity *= -1

        return plane


    def containsPoint(self, point):
        return dotProduct(self.plane.dirVec, point.location) <= self.plane.quantity