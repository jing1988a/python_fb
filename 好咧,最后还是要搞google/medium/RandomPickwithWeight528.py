# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

import random

class Solution(object):

#     def __init__(self, w):
#         """
#         :type w: List[int]
#         """
#         self.w=w
#         self.totalWeight=sum(w)


#     def pickIndex(self):
#         """
#         :rtype: int
#         """
#         rand=random.randint(1 ,self.totalWeight)
#         i=0
#         while rand>0:
#             rand-=self.w[i]
#             i+=1
#         return i-1


# above O(n) below O(log(n))

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.preSum=[]
        cur=0
        for weight in w:
            cur+=weight
            self.preSum.append(cur)

        self.totalWeight=sum(w)


    def pickIndex(self):
        """
        :rtype: int
        """
        rand=random.randint(1 ,self.totalWeight)
        i=0
        start=0
        end=len(self.preSum)
        while start<end:
            mid=(start+end)//2
            if self.preSum[mid]==rand:
                return mid
            elif self.preSum[mid]<rand:
                start=mid+1
            else:
                end=mid
        return start




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()