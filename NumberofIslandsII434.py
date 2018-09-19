"""
Definition for a point.

"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        u=Union()
        ans=[]
        matrix=[[0 for _ in range(m)] for _ in range(n)]
        for o in operators:
            oIdx=o.x*m+o.y
            po=u.findP(oIdx)
            matrix[o.x][o.y]=1
            for t1,t2 in [[1,  0] , [-1 , 0] , [0 , 1] , [0 , -1]]:
                a=o.x+t1
                b=o.y+t2
                if 0<=a<n and 0<=b<m and matrix[a][b]==1:
                    qIdx=a*m+b
                    pq=u.findP(qIdx)
                    u.unionP(pq , po)
            print(u.totalP)
            ans.append(u.totalP)
        return ans

class Union:
    d=dict()
    totalP=0
    def findP(self , v):
        if not v in self.d:
            self.d[v]=v
            self.totalP+=1
        if self.d[v]==v:
            return v

        p=self.findP(self.d[v])
        self.d[v]=p
        return p
    def unionP(self , a , b):
        if a==b:
            return
        self.d[a]=b
        self.totalP-=1   


test=Solution()
print(test.numIslands2(4,  5 , [Point(1,1),Point(1,2),Point(1,3),Point(1,4)]))