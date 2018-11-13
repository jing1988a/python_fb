# You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.
#
# Example
# Example 1:
#
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Notice
# the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
#

import sys
import heapq


class Solution:
    """
    @param nums: k lists of sorted integers
    @return: the smallest range that includes at least one number from each of the k lists
    """

    def smallestRange(self, nums):
        # write your code here
        l = len(nums)
        if l < 2:
            return [nums[0][0], nums[0][0]]
        curMax = -sys.maxsize
        hq = []
        curLen = sys.maxsize
        ans = [None, None]
        for i in range(l):
            heapq.heappush(hq, (nums[i][0], i, 0))
            curMax = max(curMax, nums[i][0])
        while True:
            v, n, m = heapq.heappop(hq)
            if curLen > curMax - v:
                ans = [v, curMax]
                curLen = curMax - v
            if m == len(nums[n]) - 1:
                return ans

            nextV = nums[n][m + 1]
            curMax = max(curMax, nextV)
            heapq.heappush(hq, (nextV, n, m + 1))
        return ans
