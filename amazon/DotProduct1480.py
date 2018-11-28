# Given two array, find their dot product.(Wikipedia)
#
# Example
# Input:A = [1,1,1]
# B = [2,2,2]
# Output:6
# Notice
# if there is no dot product, return -1.
#

class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """

    def dotProduct(self, A, B):
        la=len(A)
        lb=len(B)
        if la!=lb or la==0:
            return -1
        ans=0
        for i in range(la):
            ans+=A[i]*B[i]
        return ans



# Write your code here
