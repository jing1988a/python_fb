class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """
    def totalHammingDistance(self, nums):
        # Write your code here
        l=len(nums)
        ans=0
        for i in range(32):
            mask=1<<i
            count=0
            for n in nums:
                if n&mask:
                    count+=1
            ans+=count*(l-count)
        return ans