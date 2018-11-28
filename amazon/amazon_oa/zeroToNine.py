# 第二题 二维图从[0,0] 出发，0表示点不能去，1 表示能去，找去目标点的最短路径，常规bfs


class Problem:
    def solve(self, matrix, end):
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        if m == 0:
            return []
        candidate = []
        visited = [[False for _ in range(m)] for _ in range(n)]
        ans = []
        q = [[[0, 0], [[0, 0]]]]
        visited[0][0] = True
        while q:
            p = []
            # print(q)
            for cur, path in q:
                # print(cur)
                # print(path)
                if cur == end:
                    return path

                for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nextI = cur[0] + x
                    nextJ = cur[1] + y
                    if 0 <= nextI < n and 0 <= nextJ < m and matrix[nextI][nextJ] != 1 and not visited[nextI][nextJ]:
                        visited[nextI][nextJ] = True
                        p.append([[nextI, nextJ], path + [[nextI, nextJ]]])
            q = p
        return []


matrix = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1]]
test = Problem()
print(test.solve(matrix, [3, 0]))


# 0, 0, 0, 0
# 0, 1, 1, 0
# 0, 0, 0, 0
# 0, 1, 1, 1


# stright forward BFS question. if you know BFS then it is easy
# otherwise it is hard.
# tricky part to how to store the path. I used a brute force way to store the path
# for every node , which to be honest is not very space efficent. a better way would be store its previews node
# and when we found a valid anser, traceback to the original node and generate the answer
# but requires extra code and more likely to have bugs. since the time is limited so i decided to go the safer way and sacrifice space efficiency
