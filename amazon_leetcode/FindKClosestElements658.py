# Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
import collections


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ans = collections.deque()
        for v in arr:
            if len(ans) < k:
                ans.append(v)
            else:
                if abs(v - x) > abs(ans[0] - x):
                    break
                elif abs(v - x) < abs(ans[0] - x):
                    ans.popleft()
                    ans.append(v)
        return list(ans)

        # [0,0,0,1,3,5,6,7,8,8]
        # 2
        # 2
