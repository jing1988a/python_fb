# Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).
#
# You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
#
#
#
# Example 1:
#
# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
#
# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1


class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        cur=1
        while reader.get(cur-1)!=2147483647:
            temp=reader.get(cur-1)
            if temp==target:
                return cur-1
            elif temp>target:
                break
            cur*=2
        startIdx=cur/2-1
        endIdx=cur-1

        return self.bSearch(reader , target , startIdx , endIdx)
    def bSearch(self , reader , target , startIdx , endIdx):
        while startIdx<endIdx:
            midIdx=(startIdx+endIdx)//2
            midV=reader.get(midIdx)
            if midV==target:
                return midIdx
            if midV>target:
                endIdx=midIdx-1
            else:
                startIdx=midIdx+1
        if reader.get(startIdx)==target:
            return startIdx
        return -1