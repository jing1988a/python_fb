"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        ans=[]
        self.preorder(root , ans)
        return ans
    def preorder(self , root , ans):
        if not root:
            return
        ans.append(root.val)
        self.preorder(root.left , ans)
        self.preorder(root.right , ans)