# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
#
# Example:
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Note:
#
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
#
#

class Solution:
    def __init__(self):
        self.ans=False

    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        l=len(start)
        visited=set()
        self.dfs(start , end , visited , l)
        return self.ans
    def dfs(self, start , end , visited , l):
        visited.add(start)
        if self.ans:
            return
        if start==end:
            self.ans=True
        for i in range(l):
            if start[i]=='R':
                if i+1<l and start[i+1]=='X':
                    temp=start[:i]+'XR'+start[i+2:]
                    if not temp in visited:
                        self.dfs(temp , end , visited , l)
            elif start[i]=='L':
                if i-1>=0 and start[i-1]=='X':
                    temp=start[:i-1]+"LX"+start[i+1:]
                    if not temp in visited:
                        self.dfs(temp , end , visited , l)

