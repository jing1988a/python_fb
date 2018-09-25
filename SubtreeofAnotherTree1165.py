"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    ans=False
    def isSubtree(self, s, t):
        # Write your code here
        if t is None:
            if s is None:
                return True
            return False

        self.recur(s , t)
        return self.ans
    def recur(self , s , t):
        if s is None:
            return
        if s.val==t.val:
            if self.isSameTree(s , t):
                self.ans=True
        if self.ans:
            return
        self.recur(s.left , t)
        self.recur(s.right , t)
    def isSameTree(self , s , t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val==t.val:
            return self.isSameTree(s.left , t.left) and self.isSameTree(s.right , t.right)
        else:
            return False