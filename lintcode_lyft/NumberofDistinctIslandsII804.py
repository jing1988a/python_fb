# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).
#
# Example
# Example 1:
#
# 11000
# 10000
# 00001
# 00011
# Given the above grid map, return 1.
#
# Notice that:
#
# 11
# 1
# and
#
#  1
# 11
# are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
#
# Example 2:
#
# 11100
# 10001
# 01001
# 01110
# Given the above grid map, return 2.
#
# Here are the two distinct islands:
#
# 111
# 1
# and
#
# 1
# 1
# Notice that:
#
# 111
# 1
# and
#
# 1
# 111
# are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
#
# Notice
# The length of each dimension in the given grid does not exceed 50
#
#

class Solution:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    def numDistinctIslands2(self, grid):
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
            if self.rotate0(i) or self.rotate90(i) in temp or self.rotate180(i) in temp or self.rotate270(i) in temp:
                continue
            temp.add(tuple((x - firstNodeRow) * m + y - firstNodeCol for x, y in i))
        return len(temp)

    def rotate0(self , nodes):
        firstNodeRow = nodes[0][0]
        firstNodeCol = nodes[0][1]
        return tuple((x - firstNodeRow) * m + y - firstNodeCol for x, y in nodes)
    def rotate90(self , nodes):
        firstNodeRow = nodes[0][0]
        firstNodeCol = nodes[0][1]
        newNodes=[ [x-firstNodeRow , y-firstNodeCol] for x , y in nodes ]

        return tuple()


test = Solution()
print(test.numberofDistinctIslands([[1, 1, 0, 0, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 1, 0, 1, 1]]))

