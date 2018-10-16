# There is a list composed by sets. If two sets have the same elements, merge them. In the end, there are several sets left.
#
# Example
# Given list = [[1,2,3],[3,9,7],[4,5,10]], return 2.
#
# Explanation:
# There are 2 sets of [1,2,3,9,7] and [4,5,10] left.
# Given list = [[1],[1,2,3],[4],[8,7,4,5]], return 2.
#
# Explanation:
# There are 2 sets of [1,2,3] and [4,5,7,8] left.
# Notice
# The number of sets n <=1000.
# The number of elements for each set m <= 100.
# The element must be a non negative integer and not greater than 100000.



class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        u=Union()
        for s in sets:
            p1=u.findP(s[0])
            for i in range(1  , len(s)):
                p2=u.findP(s[i])
                u.unionP(p2 , p1)
        return u.totalSet


class Union:
    def __init__(self ):
        self.d=dict()
        self.totalSet=0
    def findP(self , v):
        if not v in self.d:
            self.d[v]=v
            self.totalSet+=1
        if self.d[v]==v:
            return v

        p=self.findP(self.d[v])
        self.d[v]=p
        return p
    def unionP(self , p2 , p1):
        if p1==p2:
            return
        self.d[p2]=p1
        self.totalSet-=1