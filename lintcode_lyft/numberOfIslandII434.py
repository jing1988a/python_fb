# Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.
#
# Example
# Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].
#
# return [1,1,2,2].
#
# Notice
# 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        if n <= 0 or m <= 0:
            raise Exception('invalid input')
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        u = Union()
        ans = []
        for o in operators:
            # can i assume operators contain valid input and will not be out of range?
            i = o.x
            j = o.y
            matrix[i][j] = 1
            p1 = u.findP(i * m + j)
            for x, y in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                ni = i + x
                nj = j + y
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                    p2 = u.findP(ni * m + nj)
                    u.unionP(p2, p1)
            ans.append(u.totalIsland)
        return ans


class Union:
    def __init__(self):
        self.u = dict()
        self.totalIsland = 0

    def findP(self, v):
        if not v in self.u:
            self.u[v] = v
            self.totalIsland += 1
        if self.u[v] == v:
            return v
        p = self.findP(self.u[v])
        self.u[v] = p
        return p

    def unionP(self, p2, p1):
        if p2 == p1:
            return
        self.u[p2] = p1
        self.totalIsland -= 1
