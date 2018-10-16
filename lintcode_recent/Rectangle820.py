# Give a set, if you can find four points that make up a rectangle that is parallel to the coordinate axis and outputs YES or NO.
#
# Example
# Given set = [[0,0],[0,1],[1,1],[1,0]], return YES.
#
# Explanation:
# We can find four points that make up a rectangle which is parallel to the coordinate axis.
# Given set = [[0,0],[0,1],[1,1],[2,0]], return NO.
#
# Explanation:
# We can not find four points that meet the conditions.
# Notice
# The number of points in the set is less than 2000, and the coordinate range is [-10000000,10000000].




"""
class Point:
    def __init__( self, x=0, y=0):
       	self.x = x
       	self.y = y
"""
class Point:
    def __init__( self, x=0, y=0):
       	self.x = x
       	self.y = y
class Solution:
    """
    @param pointSet: The point set
    @return: The answer
    """
    def rectangle(self, pointSet):
        # Write your code here
        # a=(1 , 1)
        # b=(1 , 1)
        # c=set()
        # c.add(a)
        # print((1 , 1) in c)
        s=set()
        for p in pointSet:
            s.add((p.x , p.y))
        print(s)
        for p in s:
            for q in s:
                if p[0]==q[0] or p[1]==q[1]:
                    continue
                if (p[0] , q[1]) in s and (q[0] , p[1]) in s:
                    return 'YES'
        return "NO"