# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
#


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n=len(M)
        if n==0:
            return 0
        m=len(M[0])
        if m==0:
            return 0
        ans=0
        for i in range(n):
            for j in range(m):
                if M[i][j]==1:
                    if i==0 or (i-1>=0 and M[i-1][j]!=1):
                        ans=max(ans , self.checkVertical(M , i , j))
                    if j==0 or (j-1>=0 and M[i][j-1]!=1):
                        ans=max(ans , self.checkHorizental(M , i , j))
                    if i==0 or j==0 or (i>=1 and j>=1 and M[i-1][j-1]!=1):
                        ans=max(ans , self.checkDiagonal(M , i , j))
                    if i==0 or j==m-1 or (i>=1 and j<m-1 and M[i-1][j+1]!=1):
                        ans=max(ans , self.checkDiagonalReverse(M , i , j))
        return ans
    def checkVertical(self , M , i , j):
        ans=0
        for x in range(i , len(M)):
            if M[x][j]==1:
                ans+=1
            else:
                break
        return ans
    def checkHorizental(self , M , i , j):
        ans=0
        for x in range(j , len(M[0])):
            if M[i][x]==1:
                ans+=1
            else:
                break
        return ans
    def checkDiagonal(self , M , i , j):
        ans=0
        x=0

        while i+x<len(M) and j+x<len(M[0]):
            if M[i+x][j+x]==1:
                ans+=1
            else:
                break
            x+=1
        return ans
    def checkDiagonalReverse(self , M , i , j):
        ans=0
        x=0

        while i+x<len(M) and j-x>=0:
            if M[i+x][j-x]==1:
                ans+=1
            else:
                break
            x+=1
        return ans

