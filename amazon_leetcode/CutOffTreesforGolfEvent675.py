# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.
#
# Example 1:
# Input:
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
# Example 2:
# Input:
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
# Example 3:
# Input:
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
# Hint: size of the given matrix will not exceed 50x50.
import heapq


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        n = len(forest)
        if n == 0:
            return 0
        m = len(forest[0])
        if m == 0:
            return 0
        ans = 0
        cur1 = 0
        cur2 = 0
        q = self.getHq(forest)
        #print(q)
        while q:
            #print(q)
            v, t1, t2 = heapq.heappop(q)
            if v == 1:
                return ans
            steps = self.moveAndCut(cur1, cur2, t1, t2, forest, n, m)
            #print(steps)
            if steps == -1:
                return -1
            ans += steps
            cur1=t1
            cur2=t2
        return ans

    def getHq(self, forest):
        hq = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    hq.append((forest[i][j], i, j))
        heapq.heapify(hq)
        return hq

    def moveAndCut(self, cur1, cur2, t1, t2, forest, n, m):
        steps = 0
        q = [[cur1, cur2]]
        visited = [[False for j in range(m)] for i in range(n)]

        while q:
            p = []
            for c in q:
                visited[c[0]][c[1]] = True
                if c[0] == t1 and c[1] == t2:
                    return steps
                for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nextI = c[0] + x
                    nextJ = c[1] + y
                    if 0 <= nextI < n and 0 <= nextJ < m and forest[nextI][nextJ] != 0 and not visited[nextI][nextJ]:
                        p.append([nextI, nextJ])
            q=p
            steps+=1
        return -1


test=Solution()
print(test.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
