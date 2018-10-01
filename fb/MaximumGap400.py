class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        nums.sort()
        ans=0
        l=len(nums)
        for i in range(1 , l):
            ans=max(ans , nums[i]-nums[i-1])
        return ans