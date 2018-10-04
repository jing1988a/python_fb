# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# Note:
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        a = []
        if p1 in a:
            return False
        a.append(p1)
        if p2 in a:
            return False
        a.append(p2)
        if p3 in a:
            return False
        a.append(p3)
        if p4 in a:
            return False
        a.append(p4)
        a.sort(key=lambda x: (x[0], x[1]))
        return (pow(a[0][0] - a[1][0], 2) + pow(a[0][1] - a[1][1], 2)) == (
        pow(a[0][0] - a[2][0], 2) + pow(a[0][1] - a[2][1], 2)) == (
               pow(a[3][0] - a[1][0], 2) + pow(a[3][1] - a[1][1], 2)) == (
               pow(a[3][0] - a[2][0], 2) + pow(a[3][1] - a[2][1], 2)) and (pow(a[0][0] - a[3][0], 2) + pow(
            a[0][1] - a[3][1], 2)) == (pow(a[2][0] - a[1][0], 2) + pow(a[2][1] - a[1][1], 2))