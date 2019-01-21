# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
#
#
# Example 1:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
#
# Note:
#
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
import sys
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pointMap=set()
        for point in points:
            pointMap.add( (point[0] , point[1]) )
        ans=sys.maxsize
        for i in range(len(points)-1):
            for j in range(i+1 , len(points)):
                p1=points[i]
                p2=points[j]
                if p1[0]==p2[0] or p1[1]==p2[1]:
                    continue
                p3=(p1[0] , p2[1])
                p4=(p2[0] , p1[1])
                if p3 in pointMap and p4 in pointMap:
                    ans=min(ans , abs(p1[0]-p2[0])*abs(p1[1]-p2[1])  )
        return ans if ans!=sys.maxsize else 0