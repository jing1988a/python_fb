# Give an integer array，find the longest increasing continuous subsequence in this array.
#
# An increasing continuous subsequence:
#
# Can be from right to left or from left to right.
# Indices of the integers in the subsequence should be continuous.
# Example
# For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.
#
# For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
#
# Challenge
# O(n) time and O(1) extra space.


class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        l=len(A)
        if l<2:
            return l
        flag=0
        count=1
        ans=0
        i=1
        while i < l:
            if A[i]<A[i-1]:
                if flag==-1:
                    count+=1
                elif flag==0:
                    flag=-1
                    count+=1
                else:
                    ans=max(ans , count)
                    count=2
                    flag=-1
            elif A[i]>A[i-1]:
                if flag==1:
                    count+=1
                elif flag==0:
                    count+=1
                    flag=1
                else:
                    ans=max(ans , count)
                    count=2
                    flag=1
            i+=1
        ans=max(ans , count)
        return ans