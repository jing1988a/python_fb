# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Notice that:
#
# 11
# 1
# and
#
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
#


class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """

    def numberofDistinctIslands(self, grid):
        # write your code here
        # 1 find all island
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        islands = self.getAllIsland(grid, n, m)
        # 2 check if they are same
        return self.countIsland(islands, m)

    def getAllIsland(self, grid, n, m):
        islands = []
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    nodes = []
                    self.dfs(grid, visited, i, j, n, m, nodes)
                    islands.append(nodes)
        return islands

    def dfs(self, grid, visited, i, j, n, m, nodes):
        nodes.append([i, j])
        visited[i][j] = True
        for x, y in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nextI = i + x
            nextJ = j + y
            if 0 <= nextI < n and 0 <= nextJ < m and grid[nextI][nextJ] == 1 and not visited[nextI][nextJ]:
                self.dfs(grid, visited, nextI, nextJ, n, m, nodes)

    def countIsland(self, islands, m):
        temp = set()
        for i in islands:
            firstNodeRow = i[0][0]
            firstNodeCol = i[0][1]
            temp.add(tuple((x - firstNodeRow) * m + y - firstNodeCol for x, y in i))
        return len(temp)


test=Solution()
print(test.numberofDistinctIslands([[1,1,0,0,1],[1,0,0,0,0],[1,1,0,0,1],[0,1,0,1,1]]))
