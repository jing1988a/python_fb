class Solution:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    ans=0
    def findTargetSumWays(self, nums, s):
        # Write your code here
        l=len(nums)
        self.recur(nums , 0 , 0 , s , l)
        return self.ans
    def recur(self , nums , idx , cur , s , l):
        if idx==l:
            if cur==s:
                self.ans+=1
            return
        self.recur(nums , idx+1 , cur+nums[idx] , s , l)
        self.recur(nums  , idx+1 , cur-nums[idx] , s , l)