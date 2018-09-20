class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        n=len(grid)
        if n==0:
            return 0
        m=len(grid[0])
        if m==0:
            return 0
        dp=[[0 for _ in range(m)] for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(1 , n):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1 , m):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1 , n):
            for j in range(1 , m):
                dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        return dp[-1][-1]


test=Solution()
test.minPathSum([[1,2],[1,1]])