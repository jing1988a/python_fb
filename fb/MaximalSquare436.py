class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        n=len(matrix)
        if n==0:
            return 0
        m=len(matrix[0])
        if m==0:
            return 0
        dp=[[0 for i in range(m)] for j in range(n)]
        ans=0
        for i in range(n):
            if matrix[i][0]==1:
                dp[i][0]=1
                ans=1
        for j in range(m):
            if matrix[0][j]==1:
                dp[0][j]=1
                ans=1
        for i in range(1 ,  n):
            for j in range(1 , m ):
                if matrix[i][j]==1:
                    dp[i][j]=min(dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1] )+1
                    ans=max(ans , dp[i][j])
        return ans*ans