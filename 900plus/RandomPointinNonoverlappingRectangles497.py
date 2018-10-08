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


class Solution:
    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.l = len(rects)
        self.size = []
        self.total = 0
        for r in rects:
            cur = (r[3] - r[1]) * (r[2] - r[0])
            self.size.append(cur)
            self.total += cur

    def pick(self):
        """
        :rtype: List[int]
        """
        target = random.randint(1, self.total)
        cur = 0
        i = 0
        while i < self.l:
            cur += self.size[i]
            if cur >= target:
                return [random.randint(self.rects[i][0], self.rects[i][2]),
                        random.randint(self.rects[i][1], self.rects[i][3])]
