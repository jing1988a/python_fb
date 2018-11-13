class Solution:
    def Find2rdLargest(self , root):
        self.count=0
        self.ans=None
        self.recur(root)
        return self.ans
    def recur(self , node):
        if not node or self.count>2:
            return
        self.recur(node.right)
        self.count+=1
        if self.count==2:
            self.ans=node.val
            self.count=10
            return
        self.recur(node.left)