# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
#
# Note:
# A subtree must include all of its descendants.
#
# Example:
#
# Input: [10,5,15,1,8,null,7]
#
#    10
#    / \
#   5  15
#  / \   \
# 1   8   7
#
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?



# Definition for a binary tree node.






#
# class Solution(object):
#     def __init__(self):
#         self.ans=0
#     def largestBSTSubtree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         self.recurCheck(root)
#         return self.ans
#     def recurCheck(self , root):
#         if not root:
#             return
#         count=self.checkBST(root , -sys.maxsize , sys.maxsize )
#         self.ans=max(self.ans , count)
#         self.recurCheck(root.left)
#         self.recurCheck(root.right)
#     def checkBST(self , root , leftV , rightV):
#         if not root:
#             return 0
#         if root.val<=leftV or root.val>=rightV:
#             return -1
#
#         countLeft=self.checkBST(root.left , leftV , root.val)
#         countRight=self.checkBST(root.right , root.val , rightV)
#         if countLeft==-1 or countRight==-1:
#             return -1
#         else:
#             return 1+countLeft+countRight



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



import sys

class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        TreeMax , TreeMin , count=self.recurCheck(root)
        return count
    def recurCheck(self , root):
        if not root:
            return sys.maxsize , -sys.maxsize , 0

        leftTreeMin , leftTreeMax , leftCount=self.recurCheck(root.left)
        rightTreeMin , rightTreeMax , rightCount=self.recurCheck(root.right)
        if root.val<=leftTreeMax or root.val>=rightTreeMin:
            return -sys.maxsize , sys.maxsize , max( leftCount ,  rightCount)
        else:
            return min(root.val ,  leftTreeMin) , max(root.val , rightTreeMax) , 1+rightCount+leftCount

