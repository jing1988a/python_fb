# Given two arrays, write a function to compute their intersection.
#
# Example
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Challenge
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to num2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# Notice
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
#
import collections
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        s=collections.Counter(nums1)
        ans=[]
        for n in nums2:
            if n in s:
                ans.append(n)
                s[n]-=1
                if s[n]==0:
                    del s[n]
        return ans
