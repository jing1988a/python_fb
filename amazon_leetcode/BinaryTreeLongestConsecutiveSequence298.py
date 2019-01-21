# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# Example 1:
#
# Input:
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# Output: 3
#
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:
#
# Input:
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# Output: 2
#
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.ans=0
    def longestConsecutive(self, root):

        self.recur(root)
        return self.ans

    def recur(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        seq = 1
        lSeq = self.longestConsecutive(root.left)
        rSeq = self.longestConsecutive(root.right)
        if root.left and root.left.val == (root.val + 1):
            seq = lSeq + 1
        if root.right and root.right.val == (root.val + 1):
            seq = max(seq, 1 + rSeq)
        self.ans = max(self.ans, seq)
        # print('root.val='+str(root.val))
        # print(seq)
        # print(self.ans)
        # print( ' ')
        return seq


a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(2)
d = TreeNode(3)
a.left = b
a.right = c
c.right=d

test = Solution()
print(test.longestConsecutive(a))
