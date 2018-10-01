

import sys

class Solution:
    """
    @param nums: a list of integers
    @param m: an integer
    @return: return a integer
    """
    def splitArray(self, nums, m):
        # write your code here
        # dp[n][m] n is length of nums , m is part
        # dp[i][j]=min(dp[i][j] , max(dp[x][j-1] , new subarray) ) for x in range(1 , i)

        l=len(nums)
        dp=[[sys.maxsize for _ in range(m+1)] for _ in range(l)]
        cur=0
        for i in range(l):
            cur+=nums[i]
            dp[i][1]=cur
        for j in range(2 , m+1):
            for i in range(1 , l):
                cur=0
                for x in range(i):
                    cur+=nums[i-x]
                    temp=max(dp[i-x-1][j-1] , cur)
                    if temp<dp[i][j]:
                        dp[i][j]=temp
                    else:
                        break

        # print(dp)
        return dp[l-1][m]


test = Solution()
print(test.splitArray([1, 4, 4], 3))
