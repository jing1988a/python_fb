
import bisect

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        # return bisect.bisect_left(A , target)

        e=len(A)-1
        s=0
        while s<=e:
            m=(s+e)//2
            if A[m]==target:
                return m
            elif A[m]>target:
                e=m-1
            else:
                s=m+1
        return s