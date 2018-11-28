# Given a BST, find the path with the minimum sum from root to leaves.
#
# Example
# Input:{5,2,6,#,3,#,8}
# Output:10
#
#


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
    @param root: the root
    @return: minimum sum
    """
    def minimumSum(self, root):
        # Write your code here
        ans=[sys.maxsize]
        self.recur(root , 0 , ans)
        return ans[0]
    def recur(self , root , cur , ans):
        if not root:

            return
        cur+=root.val

        if root.left:
            self.recur(root.left ,cur , ans)
        if root.right:
            self.recur(root.right, cur, ans)
        if not root.left and not root.right:
            ans[0]=min(ans[0] ,  cur)


