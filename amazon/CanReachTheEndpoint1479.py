# Given a map size of m*n, 1 means space, 0 means obstacle, 9 means the endpoint. You start at (0,0) and return whether you can reach the endpoint.
#
# Example
# Input:[[1,1,1],[1,1,1],[1,1,9]]
# Output:true


class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        n=len(map)
        if n==0:
            return False
        m=len(map[0])
        if m==0:
            return False
        visited=[[False for _ in range(m)] for _ in range(n)]
        self.ans=False
        self.recur(0 , 0 , n , m , map , visited )
        return self.ans
    def recur(self , i  , j , n  , m  , map , visited):
        if self.ans==True:
            return
        if map[i][j]==9:
            self.ans=True
            return
        visited[i][j] = True
        for x , y in [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]:
            nextI=i+x
            nextJ=j+y
            if 0<=nextI<n and 0<=nextJ<m and map[nextI][nextJ]!=0 and visited[nextI][nextJ]==False:
                self.recur(nextI, nextJ, n, m , map , visited)
        visited[i][j]=False

