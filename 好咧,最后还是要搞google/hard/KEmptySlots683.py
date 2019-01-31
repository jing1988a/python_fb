# Approach #1: Insert Into Sorted Structure [Accepted]
# Intuition
#
# Let's add flowers in the order they bloom. When each flower blooms, we check it's neighbors to see if they can satisfy the condition with the current flower.
#
# Algorithm
#
# We'll maintain active, a sorted data structure containing every flower that has currently bloomed. When we add a flower to active, we should check it's lower and higher neighbors. If some neighbor satisfies the condition, we know the condition occurred first on this day.
#
#
# Approach #2: Min Queue [Accepted]

#
# intuition
#
# For each contiguous block ("window") of k positions in the flower bed, we know it satisfies the condition in the problem statement if the minimum blooming date of this window is larger than the blooming date of the left and right neighbors.
#
# Because these windows overlap, we can calculate these minimum queries more efficiently using a sliding window structure.
#
# Algorithm
#
# Let days[x] = i be the time that the flower at position x blooms. For each window of k days, let's query the minimum of this window in (amortized) constant time using a MinQueue, a data structure built just for this task. If this minimum is larger than it's two neighbors, then we know this is a place where "k empty slots" occurs, and we record this candidate answer.
#
# To operate a MinQueue, the key invariant is that mins will be an increasing list of candidate answers to the query MinQueue.min.
#
# For example, if our queue is [1, 3, 6, 2, 4, 8], then mins will be [1, 2, 4, 8]. As we MinQueue.popleft, mins will become [2, 4, 8], then after 3 more popleft's will become [4, 8], then after 1 more popleft will become [8].
#
# As we MinQueue.append, we should maintain this invariant. We do it by popping any elements larger than the one we are inserting. For example, if we appended 5 to [1, 3, 6, 2, 4, 8], then mins which was [1, 2, 4, 8] becomes [1, 2, 4, 5].
#
# Note that we used a simpler variant of MinQueue that requires every inserted element to be unique to ensure correctness. Also, the operations are amortized constant time because every element will be inserted and removed exactly once from each queue.
#
#
# from collections import deque
# class MinQueue(deque):
#     def __init__(self):
#         deque.__init__(self)
#         self.mins = deque()
#
#     def append(self, x):
#         deque.append(self, x)
#         while self.mins and x < self.mins[-1]:
#             self.mins.pop()
#         self.mins.append(x)
#
#     def popleft(self):
#         x = deque.popleft(self)
#         if self.mins[0] == x:
#             self.mins.popleft()
#         return x
#
#     def min(self):
#         return self.mins[0]
#
# class Solution(object):
#     def kEmptySlots(self, flowers, k):
#         days = [0] * len(flowers)
#         for day, position in enumerate(flowers, 1):
#             days[position - 1] = day
#
#         window = MinQueue()
#         ans = len(days)
#
#         for i, day in enumerate(days):
#             window.append(day)
#             if k <= i < len(days) - 1:
#                 window.popleft()
#                 if k == 0 or days[i-k] < window.min() > days[i+1]:
#                     ans = min(ans, max(days[i-k], days[i+1]))
#
#         return ans if ans <= len(days) else -1


# Approach #3: Sliding Window [Accepted]
# As in Approach #2, we have days[x] = i for the time that the flower at position x blooms. We wanted to find candidate intervals [left, right] where days[left], days[right] are the two smallest values in [days[left], days[left+1], ..., days[right]], and right - left = k + 1.
#
# Notice that these candidate intervals cannot intersect: for example, if the candidate intervals are [left1, right1] and [left2, right2] with left1 < left2 < right1 < right2, then for the first interval to be a candidate, days[left2] > days[right1]; and for the second interval to be a candidate, days[right1] > days[left2], a contradiction.
#
# That means whenever whether some interval can be a candidate and it fails first at i, indices j < i can't be the start of a candidate interval. This motivates a sliding window approach.
#
# Algorithm
#
# As in Approach #2, we construct days.
#
# Then, for each interval [left, right] (starting with the first available one), we'll check whether it is a candidate: whether days[i] > days[left] and days[i] > days[right] for left < i < right.
#
# If we fail, then we've found some new minimum days[i] and we should check the new interval [i, i+k+1]. If we succeed, then it's a candidate answer, and we'll check the new interval [right, right+k+1].
#
# class Solution(object):
#     def kEmptySlots(self, flowers, k):
#         days = [0] * len(flowers)
#         for day, position in enumerate(flowers, 1):
#             days[position - 1] = day
#
#         ans = float('inf')
#         left, right = 0, k+1
#         while right < len(days):
#             for i in xrange(left + 1, right):
#                 if days[i] < days[left] or days[i] < days[right]:
#                     left, right = i, i+k+1
#                     break
#             else:
#                 ans = min(ans, max(days[left], days[right]))
#                 left, right = right, right+k+1
#
#         return ans if ans < float('inf') else -1
#









# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
#
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.
#
# Example 1:
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
# Example 2:
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1
# Note:
# The given array will be in the range [1, 20000].

import bisect


class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        boomingFlowers = []
        for f in flowers:
            bisect.insort(boomingFlowers, f)
            for i in range(len(boomingFlowers) - 1):
                if boomingFlowers[i + 1] - boomingFlowers[i] == k + 1:
                    return len(boomingFlowers)
        return -1


# 上面是O(n^2)

# 下面 sliding window 是 O(n)


import sys


class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        days = [0 for i in range(n + 1)]
        for i in range(flowers):
            days[flowers[i]] = i + 1
        left = 1

        ans = sys.maxsize
        while left < n - k:
            right = left + k + 1
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left = right
        return ans if ans != sys.maxsize else -1
