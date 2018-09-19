"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        # write your code here
        ans=[]
        q=[root]
        while q:
            p=[]

            curMax=-sys.maxsize
            for n in q:
                curMax=max(curMax , n.val)
                if n.left:
                    p.append(n.left)
                if n.right:
                    p.append(n.right)
            ans.append(curMax)
            q=p
        return ans