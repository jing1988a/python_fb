"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def __init__(self):
        self.ans=0
    def diameterOfBinaryTree(self, root):
        # write your code here
        if not root:
            return 0
        lMost=self.maxToLeaf(root.left)
        rMost=self.maxToLeaf(root.right)
        return max(lMost+rMost , self.ans)
    def maxToLeaf(self , root):
        if not root:
            return 0
        lMost=self.maxToLeaf(root.left)
        rMost=self.maxToLeaf(root.right)
        self.ans=max(self.ans , lMost+rMost)
        return max(lMost , rMost)+1
