class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        # write your code here
        ans = []
        self.recur(1, n, 0, k, [], ans)
        return ans

    def recur(self, idx, n, curL, k, candidate, ans):
        if curL == k:
            ans.append(candidate[::])
            return
        if n +1 - idx < k - curL:
            return
        for i in range(idx, n + 1):
            candidate.append(i)
            self.recur(i + 1, n, curL + 1, k, candidate, ans)
            candidate.pop()
test=Solution()
print(test.combine(1 ,1))
