class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        # is [1 , 2 , 1] and [1 , 1, 2] count as different?
        # assume diffrernt
        nums.sort()
        dp=[0 for i in range(target+1)]
        dp[0]=1
        for i in range(1 , target+1):
            for n in nums:
                if i-n<0:
                    break
                dp[i]+=dp[i-n]
        return dp[-1]