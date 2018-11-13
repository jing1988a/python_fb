# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.curMax = 0
        self.count = 0
        self.pre = None
        self.ans=[]

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """


        self.inOrder(root)
        if not self.pre is None:
            if self.count > self.curMax:
                self.ans = [self.pre]
            elif self.count == self.curMax:
                self.ans.append(self.pre)
        return self.ans

    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        if node.val != self.pre:
            if not self.pre is None:
                if self.count > self.curMax:
                    self.ans = [self.pre]
                    self.curMax=self.count
                elif self.count == self.curMax:
                    self.ans.append(self.pre)
            self.count = 1
        else:
            self.count += 1
        self.pre = node.val
        self.inOrder(node.right)

# class Solution(object):
#     def __init__(self):
#         self.curMax = 0
#         self.count = 0
#         self.pre = None
#
#     def findMode(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#
#         ans = []
#         self.inOrder(root, ans)
#         if not self.pre is None:
#             if self.count > self.curMax:
#                 ans = [self.pre]  所以这个BUG 可以的,  相当于是把 ans 这个指针reference 到了新地方 但是函数外面 ans 还是指向老位置
#             elif self.count == self.curMax:
#                 ans.append(self.pre)
#         return ans
#
#     def inOrder(self, node, ans):
#         if not node:
#             return
#         self.inOrder(node.left, ans)
#         if node.val != self.pre:
#             if not self.pre is None:
#                 if self.count > self.curMax:
#                     ans = [self.pre]
#                     self.curMax = self.count
#                 elif self.count == self.curMax:
#                     ans.append(self.pre)
#             self.count = 1
#         else:
#             self.count += 1
#         self.pre = node.val
#         self.inOrder(node.right, ans)


root=TreeNode(0)
a=TreeNode(1)
root.left=a
test=Solution()
print(test.findMode(root))
