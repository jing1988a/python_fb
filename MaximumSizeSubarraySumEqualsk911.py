class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        l=len(nums)
        if l==0:
            return 0
        d=dict()
        d[0]=-1
        curSum=0
        ans=0
        for i in range(l):
            curSum+=nums[i]
            if curSum-k in d:
                ans=max(ans , i-d[curSum-k])
            if curSum not in d:
                d[curSum]=i
        return ans