# Design a class to find the kth largest element in a stream. Note that it is the
# kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and an integer
#  array nums, which contains initial elements from the stream. For each call to the method
# KthLargest.add, return the element representing the kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.
#
# Accepted
# 12,360
# Submissions
# 30,377

import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # keep a min heap
        l = len(nums)
        if k < 1 or l < k - 1:
            raise Exception('invalid input')
        self.hq = []
        self.k = k
        for n in nums:
            if len(self.hq) < k:
                heapq.heappush(self.hq, n)
            else:
                if n > self.hq[0]:
                    heapq.heappushpop(self.hq, n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        if len(self.hq) < self.k:
            heapq.heappush(self.hq, val)
        else:
            if val > self.hq[0]:
                heapq.heappushpop(self.hq, val)
        return self.hq[0]


        # Your KthLargest object will be instantiated and called as such:
        # obj = KthLargest(k, nums)
        # param_1 = obj.add(val)
