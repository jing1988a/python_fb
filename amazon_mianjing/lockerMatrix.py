# 第三轮 kindle Team的BR，半小时BQ，问题是给定2D matrix和 list of coordinates 代表lockers, matrix里未指定坐标代表cities，求解所有city到最近Locker的距离，楼主给思路循环坐标list BFS，面试官提示有更好的解法，我没想出来就直接写代码了，最后提问的时候问了更好的解法是什么，面试官说可以同时对所有coordinates BFS
# diaglo is 1 step or 2 step???
import sys


class Problem:
    def solve(self, m, n, lockers):
        matrix = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        q = []
        visited = [[False for _ in range(m)] for _ in range(n)]
        for t in lockers:
            q.append(t)
            visited[t[0]][t[1]] = True
        dis = 0
        while q:
            p = []
            for temp in q:
                matrix[temp[0]][temp[1]] = dis
                for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nextI = temp[0] + x
                    nextJ = temp[1] + y
                    if 0 <= nextI < n and 0 <= nextJ < m and not visited[nextI][nextJ]:
                        p.append([nextI , nextJ])
                        visited[nextI][nextJ]=True

            q = p
            dis += 1
        return matrix


test = Problem()
print(test.solve(9, 9, [[0, 0]  , [0 , 4]  ,  [4 , 4] , [8 , 8]]))
