"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the tree after swapping
    """
    a=None
    b=None
    pre=None
    def bstSwappedNode(self, root):
        # write your code here
        self.preorder(root)
        if self.b:
            self.a.val , self.b.val=self.b.val , self.a.val
        return root
    def preorder(self , root):
        if not root:
            return
        self.preorder(root.left)
        #do
        if self.pre:
            if self.pre.val>root.val:
                self.b=root
                if not self.a:
                    self.a=self.pre
        self.pre=root
        self.preorder(root.right)