class PointCluster:
    def __init__(self, points):
        self.points = points

    # updated
    def findFarthestPoint(self, dirVec):
        farthestPoint = None
        for point in self.points:
                pointDistance = point.directionalDistance(dirVec)
                if (not farthestPoint) or (pointDistance > farthestDistance):
                    farthestPoint = point
                    farthestDistance = farthestPoint.directionalDistance(dirVec)

        return farthestPoint