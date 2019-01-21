# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
#
# What is the largest possible number of moves we can make?
#
# Example 1:
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Example 2:
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Example 3:
#
# Input: stones = [[0,0]]
# Output: 0
#
#
# Note:
#
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000




class Solution(object):
    def removeStones(self, stones):
        N=10000
        union=Union(N)
        for x , y in stones:
            px=union.find(x)
            py=union.find(y+10000)
            union.union(px , py)
        return len(stones)-len(set(union.find(x) for x , y in stones))

class Union:
    def __init__(self , n):
        self.dic=[i for i in range(N)]
    def find(self , x):
        if not self.dic[x]==x:
            px=self.find(self.dic[x])
            self.dic[x]=px
            return px
        return x
    def union(self , x , y):
        self.dic[x]=y





# class DSU:
#     def __init__(self, N):
#         self.p = [i for i in range(N)]
#
#     def find(self, x):
#         if self.p[x] != x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]
#
#     def union(self, x, y):
#         xr = self.find(x)
#         yr = self.find(y)
#         self.p[xr] = yr
#
# class Solution(object):
#     def removeStones(self, stones):
#         N = len(stones)
#         dsu = DSU(20000)
#         for x, y in stones:
#             dsu.union(x, y + 10000)
#         print(dsu.p)
#         print(list(dsu.find(x) for x, y in stones))
#         return N - len({dsu.find(x) for x, y in stones})
#
#
# test=Solution()
# print(test.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Example 3: