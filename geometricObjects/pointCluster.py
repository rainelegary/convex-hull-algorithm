class PointCluster:
    def __init__(self, points):
        self.points = points


    def findFarthestPoint(self, dirVec):
        farthestPoint = None
        for point in self.points:
                pointDistance = point.directionalDistance(dirVec)
                farthestDistance = farthestPoint.directionalDistance(dirVec)
                if (not farthestPoint) or pointDistance > farthestDistance:
                    farthestPoint = point

        return farthestPoint