# There is a one-dimensional board with a starting point on the far left side of the board and an end point on the far right side of the board. There are several positions on the board that are connected to other positions, ie if A is connected to B, then when chess falls at position A, you can choose whether to move the chess from A to B. And the connection is one way, which means that the chess cannot move from B to A. Now you have a six-sided dice, find the minimum steps to reach the end.
#
# Example
# input:
# length = 10
# connections = [[2, 10]]
# output:
# 1
# Notice
# the index starts from 1.
# length > 1
# The starting point is not connected to any other location
# connections[i][0] < connections[i][1]

import sys


class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """

    def modernLudo(self, length, connections):
        # Write your code here
        if length < 1:
            return -1
        dp = [sys.maxsize for i in range(length + 1)]
        dp[0] = 0
        dp[1]=0
        shortCut = dict()
        for c in connections:
            shortCut[c[0]] = c[1]
        i = 0
        while i <= length:

            for step in range(1, 7):
                if step+i>length:
                    break
                dp[i + step] = min(dp[i + step], dp[i] + 1)
                self.updateShortCut(dp, i + step, dp[i] + 1, shortCut)
            print(dp)
            i += 1
        return dp[-1]

    def updateShortCut(self, dp, i, step, shortCut):
        if i in shortCut:
            if dp[shortCut[i]] > step:
                dp[shortCut[i]] = step
                if shortCut[i] in shortCut:
                    self.updateShortCut(dp, shortCut[i], step, shortCut)



length = 15
connections = [[7,9],[8,14]]
test=Solution()
print(test.modernLudo(length , connections))