# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
#
#
# Note:
#
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000


class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod=10**9+7
        stack=[]
        ans=dot=0
        for i  , v in enumerate(A):
            count=1
            while stack and stack[-1][0]>=v:
                x , c =stack.pop()
                count+=c
                dot-=x*c
            stack.append([v , count])
            dot+=v*count
            ans+=dot
        return ans%mod

test=Solution()
print(test.sumSubarrayMins([3,1,2,4]))