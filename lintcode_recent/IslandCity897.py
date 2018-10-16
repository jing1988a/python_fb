# Given a matrix of size n x m, the elements in the matrix are 0、1、2. 0 for the sea, 1 for the island, and 2 for the city on the island(You can assume that 2 is built on 1, ie 2 also represents the island).
# If two 1 are adjacent, then these two 1 belong to the same island. Find the number of islands with at least one city.
#
# Example
# Given mat =
# [
#      [1,1,0,0,0],
#      [0,1,0,0,1],
#      [0,0,0,1,1],
#      [0,0,0,0,0],
#      [0,0,0,0,1]
# ]
# , return 0.
#
# Explanation:
# There are 3 islands, but none of them contain cities.
# Given mat =
# [
#      [1,1,0,0,0],
#      [0,1,0,0,1],
#      [0,0,2,1,2],
#      [0,0,0,0,0],
#      [0,0,0,0,2]
# ]
# , return 2.
#
# Explanation:
# There are 3 islands, and two of them have cities.

class Solution:
    """
    @param grid: an integer matrix
    @return: an integer
    """
    def numIslandCities(self, grid):
        # Write your code here
        n=len(grid)
        if n==0:
            return 0
        m=len(grid[0])
        if m==0:
            return 0
        ans=0
        visited=[[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]==2:
                    ans+=1
                    self.dfs(i , j , n , m , grid , visited)
        return ans
    def dfs(self , i , j , n , m , grid , visited):
        visited[i][j]=True
        for x , y in [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]:
            nextI=i+x
            nextJ=j+y
            if 0<=nextI<n and 0<=nextJ<m and not visited[nextI][nextJ] and grid[nextI][nextJ]!=0:
                self.dfs(nextI , nextJ , n , m , grid , visited)