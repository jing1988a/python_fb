class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        n=len(triangle)
        if n==0:
            return 0
        dp=[0 for _ in range(n)]
        dp[0]=triangle[0][0]
        for i in range(1 , n):
            newDp=[0 for _ in range(n)]
            for j in range(i+1):
                temp=sys.maxsize
                if j-1>=0:
                    temp=min(temp , dp[j-1])
                if j<i:
                    temp=min(dp[j] , temp)
                newDp[j]=temp+triangle[i][j]
            dp=newDp

        return min(dp)