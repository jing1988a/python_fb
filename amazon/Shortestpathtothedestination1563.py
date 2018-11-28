# Given a 2D array representing the coordinates on the map, there are only values 0, 1, 2 on the map. value 0 means that it can pass, value 1 means not passable, value 2 means target place. Starting from the coordinates [0,0],You can only go up, down, left and right. Find the shortest path that can reach the destination, and return the length of the path.
#
# Example
# Given:
#
# [
#  [0, 0, 0],
#  [0, 0, 1],
#  [0, 0, 2]
# ]
# Return: 4
#
# Notice
# 1.The map must exist and is not empty, there is only one target
#

class Solution:
    """
    @param targetMap:
    @return: nothing
    """

    def shortestPath(self, targetMap):
        # Write your code here

        n=len(targetMap)
        if n==0:
            return 0
        m=len(targetMap[0])
        if m==0:
            return 0
        q=[[0,0]]
        ans=0
        visited=[[False for _ in range(m)] for _ in range(n)]
        visited[0][0]=False
        while q:
            p=[]
            for i , j  in q:
                if targetMap[i][j]==2:
                    return ans
                for x , y in [[1  , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]:
                    nextI=i+x
                    nextJ=j+y
                    if 0<=nextI<n and 0<=nextJ<m and targetMap[nextI][nextJ]!=1 and  visited[nextI][nextJ]==False:
                        p.append([nextI , nextJ ])
                        visited[nextI][nextJ]=True
            q=p
            ans+=1
        return -1