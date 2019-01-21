# Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.
#
# Note:
#
# An integer point is a point that has integer coordinates.
# A point on the perimeter of a rectangle is included in the space covered by the rectangles.
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output:
# [null,[4,1],[4,1],[3,3]]
# Example 2:
#
# Input:
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output:
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

import random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects=rects
        curSize=0
        self.preSize=[]
        for rect in rects:
            curSize+=(rect[2]-rect[0])*(rect[3]-rect[1])
            self.preSize.append(curSize)
        self.totalSize=curSize


    def pick(self):
        """
        :rtype: List[int]
        """
        randWeight=random.randint(1 , self.totalSize)
        start=0
        end=len(self.preSize)-1
        idx=None
        while start<end:
            mid=(start+end)/2
            if self.preSize[mid]==randWeight:
                idx= mid
                break
            elif self.preSize[mid]<randWeight:
                start=mid+1
            else:
                end=mid
        if idx==None:
            idx=start
        return [random.randint(self.rects[idx][0] ,self.rects[idx][2] ) ,random.randint(self.rects[idx][1] ,self.rects[idx][3] ) ]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()