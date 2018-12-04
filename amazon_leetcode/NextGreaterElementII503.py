# Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=dict()
        nums2=nums+nums
        stack=[]
        ans=[-1 for i in range(len(nums))]
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                ans[stack.pop()]=nums2[i]
            if i<len(nums):
                stack.append(i)
            # print(ans)
            # print(stack)
        return ans



test=Solution()
print(test.nextGreaterElements([1 , 2 , 3]))


# [1, 2, 1]
# Output
# []
# Expected
# [2, -1, 2]



