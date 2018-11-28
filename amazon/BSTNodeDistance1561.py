# Given a list of numbers, construct a BST from it(you need to insert nodes one-by-one with the given order to get the BST) and find the distance between two given nodes.
#
# Example
# input:
# numbers = [2,1,3]
# node1 = 1
# node2 = 3
# output:
# 2
# Notice
# If two nodes do not appear in the BST, return -1
# We guarantee that there are no duplicate nodes in BST
# The node distance means the number of edges between two nodes


class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        if (not node1 in numbers) or (not node2 in numbers):
            return -1
        if node1 == node2:
            return 0
        root = self.constructTree2(numbers)
        LCA = self.getLCA(root, node1, node2)
        return self.getDistance(LCA, node1) + self.getDistance(LCA, node2)

    def constructTree(self, numbers):
        if not numbers:
            return None
        root = Node(numbers[0])
        i = 0
        while i < len(numbers):
            if numbers[i] > numbers[0]:
                break
            i+=1
        root.left = self.constructTree(numbers[1:i])
        root.right = self.constructTree(numbers[i:])
        return root
    def constructTree2(self , numbers):
        if len(numbers)==0:
            return None
        root=Node(numbers[0])
        for i in range(len(numbers)):
            self.add(root , numbers[i])
        return root
    def add(self , root , v):
        if v<root.val:
            if root.left is None:
                root.left=Node(v)
            else:
                self.add(root.left , v)
        elif v>root.val:
            if root.right is None:
                root.right=Node(v)
            else:
                self.add(root.right , v)
    def getLCA(self , root , n1 ,n2):
        if not root:
            return None
        if root.val==n1 or root.val==n2:
            return root
        l=self.getLCA(root.left , n1 , n2)
        r=self.getLCA(root.right , n1 , n2)
        if l and r:
            return root
        if l:
            return l
        return r
    def getDistance(self , root , v):
        dis=[0]
        self.recur(root , v , 0 , dis)
        return dis[0]
    def recur(self , root , v , cur , dis):
        if not root:
            return
        if root.val==v:
            dis[0]=cur
            return
        self.recur(root.left , v , cur+1 , dis)
        self.recur(root.right, v, cur + 1, dis)


class Node:
    def __init__(self, v=None):
        self.val = v
        self.left = None
        self.right = None

test=Solution()
print(test.bstDistance([10,18,12,16,19,13,20,3,1,7,14] , 18 , 7))

