class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        l=len(nums)
        if l<2:
            return 0
        curCount=0
        d=dict()
        d[0]=-1
        ans=0
        for i in range(l):
            if nums[i]==0:
                curCount-=1
            if nums[i]==1:
                curCount+=1
            if curCount in d:
                ans=max(ans , i-d[curCount])
            if curCount not in d:
                d[curCount]=i
        return ans