# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
#
#
# Example 1:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: 12
#
# Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
#              The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
#
# Example 2:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: -1
#
# Explanation: There is no way for the ball to stop at the destination.
#
#
#
# Note:
#
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

import sys

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        n=len(maze)
        if n==0:
            return 0
        m=len(maze[0])
        if m==0:
            return 0
        distanceMap=[[sys.maxsize for i in range(m)] for j in range(n)]
        distanceMap[start[0]][start[1]]=0
        self.recurFind(maze , start[0] , start[1] , n , m , distanceMap , destination)
        # print(distanceMap)
        return distanceMap[destination[0]][destination[1]] if distanceMap[destination[0]][destination[1]]!=sys.maxsize else -1
    def recurFind(self , maze , i , j , n , m ,distanceMap , destination):
        for x  , y in [[1 , 0 ], [-1 , 0] , [0 , -1] , [0 , 1]]:
            nextI=i+x
            nextJ=j+y
            dis=1
            while  0<=nextI<n and 0<=nextJ<m and maze[nextI][nextJ]!=1:
                nextI+=x
                nextJ+=y
                dis+=1
            nextI-=x
            nextJ-=y
            dis-=1
            if distanceMap[nextI][nextJ]>distanceMap[i][j]+dis:
                distanceMap[nextI][nextJ]=distanceMap[i][j]+dis
                self.recurFind(maze , nextI , nextJ , n , m ,distanceMap , destination)