"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: t
    @return: the sum of all left leaves
    """
    def __init__(self):
        self.ans=0
    def sumOfLeftLeaves(self, root):
        # Write your code here
        if not root:
            return self.ans
        self.traval(root.left , True)
        self.traval(root.right , False)
        return self.ans
    def traval(self , root  , flag):
        if not root:
            return
        if root.left==None and root.right==None:
            if flag:
                self.ans+=root.val
            return
        self.traval(root.left , True)
        self.traval(root.right , False)