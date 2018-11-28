import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()


# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
#

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        l=len(T)
        if l==0:
            return []
        stack=[]
        ans=[]
        for i in range(l-1 , -1 , -1):
            while stack and T[stack[-1]]<=T[i]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1]-i)
            stack.append(T[i])
        return  ans[::-1]


