class Solution:
    """
    @param N: size of 2D grid
    @param mines: in the given list
    @return: the order of the plus sign
    """

    def orderOfLargestPlusSign(self, N, mines):
        # Write your code here
        graph = self.getGraph(N, mines)
        leftMost = self.getLeft(N, graph)
        topMost = self.getTop(N, graph)
        rightMost = self.getRight(N, graph)
        bottomMost = self.getBottom(N, graph)
        ans = 0
        for i in range(N):
            for j in range(N):
                ans = max(ans, min(leftMost[i][j], rightMost[i][j], topMost[i][j], bottomMost[i][j]))
        return ans

    def getGraph(N, mines):
        return

    def getLeft(N, graph):
        return

    def getRight(N, graph):
        return

    def getTop(N, graph):
        return

    def getBottom(N, graph):
        return
