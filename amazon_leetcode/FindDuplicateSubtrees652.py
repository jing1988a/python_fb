# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node values.
#
# Example 1:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#
#       2
#      /
#     4
# and
#
#     4
# Therefore, you need to return above trees' root in the form of a list.
# Accepted
# 26,413
# Submissions
# 62,807




# Definition for a binary tree node.


import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ans=[]
        self.recur(root , ans , collections.defaultdict(int) , )
        return ans
    def recur(self , root  , ans , trees ):
        if not root:
            return '#'
        lTree=self.recur(root.left , ans , trees  )
        rTree=self.recur(root.right , ans , trees)
        curTree=str(root.val)+lTree+rTree
        if curTree in trees and trees[curTree]==1:
            ans.append(root)
        trees[curTree]+=1
        return curTree