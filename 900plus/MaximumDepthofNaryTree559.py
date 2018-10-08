#
# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# For example, given a 3-ary tree:
#
#
#
#
#
# We should return its max depth, which is 3.
#
# Note:
#
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.



"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.ans=0
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.travel(root , 0)
        return self.ans
    def travel(self , node , level):
        if not node:
            return
        level+=1
        if not node.children:
            self.ans=max(self.ans , level)
        for c in node.children:
            self.travel(c , level)

