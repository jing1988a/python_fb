# give a binary tree and start node, return the node is fartest from the start node.
import collections
class Problem:
    def solve(self , root , start):
        self.levels=collections.defaultdict(list)
        self.recur(root , 0)
        maxDis=0
        ans=None
        for leaf , l  , isLeaf in self.levels:
            if not isLeaf:
                continue
            LCA=self.getLCA(root , start , leaf )
            if self.levels[leaf.val][1]+self.levels[start.val][1]-2*self.levels[LCA.val][1]>maxDis:
                maxDis=self.levels[leaf.val][1]+self.levels[start.val][1]-2*self.levels[LCA.val][1]
                ans=leaf
        return ans
    def recur(self , root , level):
        if not root:
            return
        if not self.isLeaf(root):
            self.levels[root.val]=[root , level , False]
            self.recur(root.left , level+1 )
            self.recur(root.right , level+1)
        else:
            self.levels[root.val] = [root, level, True]
            return
    def getLCA(self , root , start , leaf):
        if not root:
            return None
        l=self.getLCA(root.left , start  , leaf)
        r=self.getLCA(root.right , start , leaf)
        if l and r:
            return root
        if l:
            return l
        if r:
            return r
        return None
