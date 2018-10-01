class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        bx=bin(x)[2:].rjust(32 , "0")
        by=bin(y)[2:].rjust(32 , "0")
        ans=0
        for i in range(32):
            if bx[i]!=by[i]:
                ans+=1
        return ans
