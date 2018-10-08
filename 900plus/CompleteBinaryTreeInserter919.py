# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
#
# Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:
#
# CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.
#
#
# Example 1:
#
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# Example 2:
#
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
#
#
# Note:
#
# The initial given tree is complete and contains between 1 and 1000 nodes.
# CBTInserter.insert is called at most 10000 times per test case.
# Every value of a given or inserted node is between 0 and 5000.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes=[]
        self.levelTravel(root)


    def levelTravel(self , root):
        if not root:
            return
        q=[root]
        while q:
            p=[]
            for n in q:
                self.nodes.append(n)
                if n.left:
                    p.append(n.left)
                if n.right:
                    p.append(n.right)
            q=p

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        temp=TreeNode(v)
        self.nodes.append(temp)
        l=len(self.nodes)
        pNode=self.nodes[l//2-1]
        if l%2:
            pNode.right=temp
        else:
            pNode.left=temp
        return pNode.val








    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0] if self.nodes else None

# a=TreeNode(1)
# b=TreeNode(2)
# c=TreeNode(3)
# d=TreeNode(4)
# e=TreeNode(5)
# f=TreeNode(6)
#
# a.left=b
# a.right=c
# b.left=d
# b.right=e
# c.left=f
test=CBTInserter(a)
test.insert(7)
print(test.get_root())


# Input:
# ["CBTInserter","insert","get_root"]
# [[[1]],[2],[]]
# Output:
# [null,1,1]
# Expected:
# [null,1,[1,2]]

# Input:
# ["CBTInserter","insert","insert","get_root"]
# [[[1,2,3,4,5,6]],[7],[8],[]]
# Output:
# [null,4,5,[1,2,3,4,5,6,null,null,7,8]]
# Expected:
# [null,3,4,[1,2,3,4,5,6,7,8]]
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()