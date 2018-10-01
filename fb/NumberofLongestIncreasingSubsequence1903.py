class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        # Write your code here
        # dp[i]=[length ,  time] that end at i
        l=len(nums)
        if l==0:
            return 0
        dp=[[1 , 1] for i in range(l)]
        maxLen=1

        for i in range(1 , l):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j][0]+1==dp[i][0]:
                        dp[i][1]+=dp[j][1]
                    elif dp[j][0]+1>dp[i][0]:
                        dp[i]=[dp[j][0]+1 , dp[j][1]]
            if dp[i][0]>maxLen:
                maxLen=dp[i][0]
        ans=0
        for d in dp:
            if d[0]==maxLen:
                ans+=d[1]
        return ans

test=Solution()
print(test.findNumberOfLIS([4,3,2,1]))