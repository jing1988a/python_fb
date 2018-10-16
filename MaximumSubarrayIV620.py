import sys

class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    import sys
    def maxSubarray4(self, nums, k):
        # write your code here
        l=len(nums)
        if l<k:
            return 0
        if l==k:
            return sum(nums)
        preSum=[0 for i in range(l+1)]
        curMin=0
        ans=-sys.maxsize
        for i in range(1 , l+1):
            preSum[i]=preSum[i-1]+nums[i-1]
            if i>=k:
                curMax=preSum[i]-curMin
                ans=max(curMax , ans)
                curMin=min(curMin , preSum[i-k+1])
        return ans