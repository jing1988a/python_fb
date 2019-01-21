# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
# Input: nums = [0, 1, 2 , 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
#

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower>upper:
            return []
        start=lower
        ans=[]
        for n in nums:
            if n>start:
                if n-1==start:
                    ans.append(str(n-1))
                else:
                    ans.append(str(start)+'->'+str(n-1))
                start=n+1

            else:
                start=n+1
        if start==upper:
            ans.append(str(start))
        elif start<upper:
            ans.append(str(start) + '->' + str(upper))
        return ans

# [0,1,3,50,75]
# 0
# 99
# Output
# ["2","2->49","51->74","76->99"]
# Expected
# ["2","4->49","51->74","76->99"]
