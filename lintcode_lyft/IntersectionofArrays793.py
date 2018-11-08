# Give a number of arrays, find their intersection, and output their intersection size.
#
# Example
# Given [[1,2,3],[3,4,5],[3,9,10]], return 1
#
# explanation:
# Only element 3 appears in all arrays, the intersection is [3], and the size is 1.
# Given [[1,2,3,4],[1,2,5,6,7][9,10,1,5,2,3]], return 2
#
# explanation:
# Only element 1,2 appear in all arrays, the intersection is [1,2], the size is 2.
# Notice
# The total number of all array elements is not more than 500000.
# There are no duplicated elements in each array.
import collections
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        n=len(arrs)
        if n==0:
            return []
        ans=0
        d=collections.defaultdict(int)
        for i in range(n):
            for j in arrs[i]:
                d[j]+=1
                if d[j]==n:
                    ans+=1
        return ans








































