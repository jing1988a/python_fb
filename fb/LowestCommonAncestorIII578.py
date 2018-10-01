"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    a=False
    b=False
    def lowestCommonAncestor3(self, root, A, B):
        self.check(root , A , B)
        if self.a and self.b:
            return self.recur(root , A , B)
        else:
            return None
    def check(self , root , A , B):
        if not root:
            return
        if root==A:
            self.a=True
        if root==B:
            self.b=True
        self.check(root.left , A , B)
        self.check(root.right , A , B)

    def recur(self, root, A, B):
        # write your code here
        if not root:
            return None
        if root==A:
            self.a=True
            return A
        if root==B:
            self.b=True
            return B
        l=self.recur(root.left ,A , B)
        r=self.recur(root.right , A , B)
        if l and r:
            return root
        if l:
            return l
        if r:
            return r