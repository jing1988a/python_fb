class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        # 1 no cycle
        # 2 only 1 connected part
        u=Union()
        for i in range(n):
            u.findP(i)
        for a , b in edges:
            pa=u.findP(a)
            pb=u.findP(b)
            if pa==pb:
                return False
            u.unionP(pa , pb)
        return u.pCount==1


class Union:
    d=dict()
    pCount=0
    def findP(self , v):
        if v not in self.d:
            self.d[v]=v
            self.pCount+=1
        if self.d[v]==v:
            return v
        pv=self.findP(self.d[v])
        self.d[v]=pv
        return pv
    def unionP(self , a , b):
        if a==b:
            return
        self.d[a]=b
        self.pCount-=1