# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
#

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        if n==0:
            return 0
        m=len(grid[0])
        if m==0:
            return 0
        visited=[[False for _ in range(m)] for _ in range(n)]
        self.ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not visited[i][j]:
                    self.count=0
                    self.dfs(grid , visited , i , j , n , m)
        return self.ans
    def dfs(self , grid , visited , i , j , n , m):
        self.count+=1
        self.ans=max(self.ans , self.count)
        visited[i][j]=True
        for x , y  in [[1 ,  0] , [-1 , 0] , [ 0 , 1] , [ 0 , -1]]:
            nextI=i+x
            nextJ=j+y
            if 0<=nextI<n and 0<=nextJ<m and visited[nextI][nextJ]==False and grid[nextI][nextJ]:
                self.dfs(grid , visited , nextI , nextJ , n , m )


