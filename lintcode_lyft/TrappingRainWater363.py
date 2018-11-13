# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# Example
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# Challenge
# O(n) time and O(1) memory
#
# O(n) time and O(n) memory is also acceptable.


class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        l=len(heights)
        if l<3:
            return 0
        lMax=0
        rMax=0
        left=0
        right=l-1
        ans=0
        while left<=right:
            if lMax<rMax:
                if lMax<=heights[left]:
                    lMax=heights[left]
                else:
                    ans+=lMax-heights[left]
                left+=1
            else:
                if rMax <= heights[right]:
                    rMax = heights[right]
                else:
                    ans += rMax - heights[right]
                right -= 1
        return ans
