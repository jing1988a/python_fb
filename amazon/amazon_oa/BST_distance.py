# Given a list of numbers, construct a BST from it and find the distance between two nodes.
# int bstDistance(int[] values, int node1, int node2)

class Problem:
    def solve(self, nums, node1, node2):
        # what if node1 or node2 not in nums?
        l = len(nums)
        if l < 2:
            return 0
        root = self.constructTree(nums)
        return self.getDis(root, node1, node2)

    def constructTree(self, nums):
        if not nums:
            return None
        root = Node(nums[0])
        i = 1
        while i < len(nums) and nums[i] < root.v:
            i += 1
        root.left = self.constructTree(nums[1:i])
        root.right = self.constructTree(nums[i:])
        return root

    def getDis(self, root, node1, node2):
        lca = self.getLCA(root, node1, node2)
        return self.disToChild(lca, node1) + self.disToChild(lca, node2)

    def getLCA(self, root, node1, node2):
        if not root:
            return None
        if root.v == node1 or root.v == node2:
            return root
        l = self.getLCA(root.left, node1, node2)
        r = self.getLCA(root.right, node1, node2)
        if l and r:
            return root
        if l:
            return l
        if r:
            return r

    def disToChild(self, node, val):
        dis = [0]
        self.recur(node, val, 0 , dis)
        return dis[0]

    def recur(self, node, val, distance , dis):
        if not node:
            return None
        if node.v == val:
            dis[0] = distance
            return
        self.recur(node.left, val, distance + 1 , dis)
        self.recur(node.right, val, distance + 1 , dis)


class Node:
    def __init__(self, v=None):
        self.v = v
        self.left = None
        self.right = None
test=Problem()
print(test.solve([5, 6 , 7] , 5 , 7))


