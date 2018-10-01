class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        l=len(nums)
        if l<2:
            return
        i=0
        cur=0
        while i<l:
            if nums[i]!=0:
                nums[cur]=nums[i]
                cur+=1
            i+=1
        while cur<l:
            nums[cur]=0
            cur+=1