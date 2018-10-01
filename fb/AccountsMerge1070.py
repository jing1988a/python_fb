import  collections
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        emailToAccount=dict()
        u=Union()
        for a in accounts:
            name=a[0]
            p1=u.findP(a[1])
            emailToAccount[a[1]]=name
            for e in a[2:]:
                p2=u.findP(e)
                emailToAccount[e]=name
                u.unionP(p2 ,  p1)
        groups=collections.defaultdict(list)
        for e in u.d:
            groups[u.findP(e)].append(e)
        ans=[]
        for e in groups:
            ans.append([emailToAccount[e]]+sorted(groups[e]))
        return ans
class Union:
    def __init__(self):
        self.d=dict()

    def findP(self , v):
        if not v in self.d:
            self.d[v]=v
        if self.d[v]==v:
            return v
        p=self.findP(self.d[v])
        self.d[v]=p
        return p
    def unionP(self , a , b):
        if a==b:
            return
        self.d[a]=b
