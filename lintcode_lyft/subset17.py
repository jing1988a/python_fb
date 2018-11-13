# Given a set of distinct integers, return all possible subsets.
#
# Example
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# Challenge
# Can you do it in both recursively and iteratively?
#
# Notice
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        # is [1 , 3] and [3 , 1] same?
        nums.sort()
        ans = []
        l = len(nums)
        self.recur(nums, 0, l, [], ans)
        return ans

    def recur(self, nums, i, l, candidate, ans):
        ans.append(candidate[::])
        if i == l:
            return
        for nextI in range(i, l):
            candidate.append(nums[nextI])
            self.recur(nums, nextI+1, l, candidate, ans )
            candidate.pop()

