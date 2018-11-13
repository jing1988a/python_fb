# Given two arrays, write a function to compute their intersection.
#
# Example
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Challenge
# Can you implement it in three different algorithms?
#
# Notice
# Each element in the result must be unique.
# The result can be in any order.

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        # write your code here
        return set(nums1) & set(nums2)

        # if it is sorted
        # l1 = len(nums1)
        # if l1 == 0:
        #     return []
        # l2 = len(nums2)
        # if l2 == 0:
        #     return []
        # i = 0
        # j = 0
        # ans = []
        # while i < l1 and j < l2:
        #     if nums1[i] == nums2[j]:
        #         ans.append(nums1[i])
        #         while i + 1 < l1 and nums1[i + 1] == nums1[i]:
        #             i += 1
        #         while j + 1 < l2 and nums2[j + 1] == nums2[j]:
        #             j += 1
        #         i+=1
        #         j+=1
        #     elif nums1[i]<nums2[j]:
        #         i+=1
        #     else:
        #         j+=1
        #
        # return ans

class Iter:

    def __init__(self , a , b):
        self.a=a
        self.b=b
        self.used=True
        self.i=0
        self.j=0
        self.findNext()

    def next(self ):
        if not self.hasNext():
            return
        temp=self.i
        self.i+=1
        self.j+=1
        self.findNext()
        return self.a[temp]
    def hasNext(self):
        return not (self.i==len(self.a) or self.j==len(self.b))

    def findNext(self):
        while self.i < len(self.a) and self.j < len(self.b):
            if self.a[self.i] == self.b[self.j]:

                while self.a[self.i] + 1 < len(self.a) and self.a[self.i + 1] == self.a[self.i]:
                    self.i += 1
                while self.b[self.j] + 1 < len(self.b) and self.b[self.j + 1] == self.b[self.j]:
                    self.j += 1
                break
            elif self.a[self.i] < self.b[self.j]:
                self.i += 1
            else:
                self.j += 1
