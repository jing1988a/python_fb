# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        self.ans=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.curIsland = []
                    self.dfs(grid, visited, i, j, n, m)
                    self.ans.add(self.mySerialize(self.curIsland ,  m ))
        print(self.ans)
        return len(self.ans)

    def dfs(self, grid, visited, i, j, n, m):
        visited[i][j] = True
        self.curIsland.append([i , j])
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nextI = i + x
            nextJ = j + y
            if 0 <= nextI < n and 0 <= nextJ < m and visited[nextI][nextJ] == False and grid[nextI][nextJ]:
                self.dfs(grid, visited, nextI, nextJ, n, m)
    def mySerialize(self , island ,  m):
        res=[]
        x=island[0][0]
        y =island[0][1]
        for i , j in island:
            res.append(str(i-x)+','+str(j-y))
        return tuple(res)

test=Solution()
print(test.numDistinctIslands([[0,1,1],[1,1,1],[0,0,0],[1,1,1],[1,1,0]]))


# [0,1,1],\
# [1,1,1],\
# [0,0,0],\
# [1,1,1],\
# [1,1,0]