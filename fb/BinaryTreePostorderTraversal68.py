"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        ans=[]
        if not root:
            return ans
        self.postOrder(root , ans)
        return ans
    def postOrder(self , root , ans):
        if not root:
            return
        self.postOrder(root.left , ans)
        self.postOrder(root.right , ans)
        ans.append(root.val)