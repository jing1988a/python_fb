# Given an array A, partition it into two (contiguous) subarrays left and right so that:
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.
#
#
#
# Example 1:
#
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:
#
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
# Note:
#
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.

# [0 3 6 6 inf]
# [5 5 5 8 8]

import sys


class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        cur = sys.maxsize
        rightMin = [0 for i in range(l)]
        leftMax = [0 for i in range(l)]
        for i in range(l - 1, -1, -1):
            rightMin[i] = cur
            cur = min(cur, A[i])
        cur = -sys.maxsize
        for i in range(l):
            cur = max(cur, A[i])
            leftMax[i] = cur
        i = 0
        while i < l:
            if rightMin[i] >= leftMax[i]:
                break
            i += 1
        return i+1

test=Solution()
print(test.partitionDisjoint([5,0,3,8,6]))
