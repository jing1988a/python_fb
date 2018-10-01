class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        # positive do not contains 0
        l=len(nums)
        if l==0:
            return -1
        start=0
        end=0
        ans=sys.maxsize
        cur=0
        while end<l:
            cur+=nums[end]
            while cur>=s:
                if(cur>=s):
                    ans=min(ans  , end-start+1)
                cur-=nums[start]
                start+=1
            end+=1
        return ans if ans!=sys.maxsize else -1