# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
#
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
#
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
#
# Note:
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.


# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        if not root:
            return []
        if root==target:
            self.findKdeepChild(root, K, ans)
            return ans

        dis = self.recur(root.left, target, K, ans)
        print(dis)
        if dis == -1:
            dis = self.recur(root.right, target, K, ans)
            if dis == -1:
                return []
            if dis + 1 == K:
                ans.append(root.val)
            elif dis + 1 < K:
                self.findKdeepChild(root.left, K - dis - 2, ans)
        else:
            if dis + 1 == K:
                ans.append(root.val)
            elif dis + 1 < K:
                self.findKdeepChild(root.right, K - dis - 2, ans)
        return ans

    def recur(self, root, target, K, ans):
        if not root:
            return -1

        if root == target:
            print(root.val)
            self.findKdeepChild(root, K, ans)
            return 0
        dis = self.recur(root.left, target, K, ans)
        if dis == -1:
            dis = self.recur(root.right, target, K, ans)
            if dis == -1:
                return -1
            if dis+1<K:
                self.findKdeepChild(root.left, K - dis - 2, ans)
        else:
            if dis+1<K:
                self.findKdeepChild(root.right, K - dis - 2, ans)
        if dis + 1 == K:
            ans.append(root.val)
        return dis + 1

    def findKdeepChild(self, root, dis, ans):
        if not root:
            return
        if dis == 0:
            ans.append(root.val)
            return
        self.findKdeepChild(root.left, dis - 1, ans)
        self.findKdeepChild(root.right, dis - 1, ans)

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right


#                     20
#             8             22
#         4      12
#              10  14
#
# 12
test=Solution()
print(test.distanceK(root, target, 2))

