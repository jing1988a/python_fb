# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# Explanation:
#
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# Follow up:

# Can you do it in time complexity O(k log mn), where k is the length of the positions?


# matrix是一行一行读进来的（用union find）


class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        union=Union()
        for p in positions:
            pIdx=p[0]*m+p[1]
            pParent=Union.findP(pIdx)
            for x , y in [[1 , 0] , [-1  , 0] , [0 , 1] , [0 , -1]]:
                neighborX=x+p[0]
                neighborY=y+p[1]
                if 0<=neighborX<n and 0<=neighborY<m:
                    neighborIdx=neighborX*m+neighborY
                    neighborParent=Union.findP(neighborIdx)
                    if neighborParent==pParent:
                        union.unionP(neighborParent , pParent)
            return union.count

class Union:

    def __init__(self):
        self.count=0
        self.dic=dict()
    def findP(self , u):
        if u not in self.dic:
            self.dic[u]=u
            self.count+=1
        if self.dic[u]==u:
            return u
        p=self.findP(self.dic[u])
        self.dic[u]=p
        return p
    def unionP(self , p1 , p2):
        if p1==p2:
            return
        self.dic[p1]=p2
        self.count-=1
        return

