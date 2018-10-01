class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, height):
        # write your code here
        stack = []
        l = len(height)
        ans = 0

        for idx, h in enumerate(height):
            curIdx = idx
            while stack and stack[-1][1] > h:
                a, b = stack.pop()
                curIdx = a
                ans = max(ans, (idx - a) * b)
            stack.append([curIdx, h])
        while stack:
            a, b = stack.pop()
            ans = max(ans, (l - a) * b)
        return ans


test=Solution()
test.largestRectangleArea([0])
