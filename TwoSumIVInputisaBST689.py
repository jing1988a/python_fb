"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """
    def __init__(self):
        self.ans=[]
    def twoSum(self, root, n):
        # write your code here
        d=set()
        self.preOrder(root , n , d)
        return self.ans if self.ans else None
    def preOrder(self , root ,n , d):
        if self.ans:
            return
        if not root:
            return
        if (n-root.val) in d:
            self.ans=[n-root.val , root.val]
        d.add(root.val)
        self.preOrder(root.left , n , d)
        self.preOrder(root.right , n , d)