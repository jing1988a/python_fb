# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example
# Given n = 12, return 3 because 12 = 4 + 4 + 4
# Given n = 13, return 2 because 13 = 4 + 9


class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        dp=[i for i in range(n+1)]
        for i in range(2 , n+1):
            j=1
            while i-j*j>=0:
                dp[i]=min(dp[i] , dp[i-j*j]+1)
                j+=1
        return dp[-1]


