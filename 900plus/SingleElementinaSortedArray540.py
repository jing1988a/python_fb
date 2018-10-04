# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        s = 0
        e = l - 1
        while s < e:
            m = (s + e) // 2
            if nums[m - 1] != nums[m] and nums[m + 1] != nums[m]:
                return nums[m]
            if m - 1 >= 0 and nums[m - 1] == nums[m]:
                if (m + 1) % 2 == 0:
                    s = m + 1
                else:
                    e = m - 1
            if m + 1 < l and nums[m + 1] == nums[m]:
                if (m + 1) % 2 == 0:
                    e = m - 1
                else:
                    s = m + 1

        return nums[e]


test = Solution()
print(test.singleNonDuplicate([1, 1, 2, 2, 4, 4, 5, 5, 9]))



# Line 14: IndexError: list index out of range
