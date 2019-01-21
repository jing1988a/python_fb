# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.recurFind(nums, 0, [], ans, k, n)
        return ans

    def recurFind(self, nums, idx, candidate, ans, k, n):
        if k == 0 and n == 0:
            ans.append(candidate[::])
        if k == 0 or n == 0:
            return
        for i in range(idx, 9):
            candidate.append(nums[i])
            self.recurFind(nums, i + 1, candidate, ans, k - 1, n - nums[i])
            candidate.pop()


test = Solution()
print(test.combinationSum3(3, 7))
