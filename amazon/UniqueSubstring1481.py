# Description
# Given a string s, find all the unique substring with the length of k and sort the results in lexicographic order.
#
# Have you met this question in a real interview?
# Example
# Input: s = "caaab"
# k = 2
# Output:["aa","ab","ca"]

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: all unique substring
    """
    def uniqueSubstring(self, s, k):
        l=len(s)
        if l<k:
            return []
        ans=set()
        for i in range(l-k+1):
            ans.add(s[i:k+i])
        return sorted(list(ans))



    def uniqueSubSeqence(self, s, k):
        # Write your code here
        ans = set()
        l = len(s)
        if l < k:
            return []
        self.recur(s, 0, 0, k, l, [], ans)
        return sorted(list(ans))

    def recur(self, s, idx, cur, k, l, candidate, ans):
        if cur == k:
            ans.add(''.join(candidate))
            return
        if idx == l:
            return
        if l - idx < k - cur:
            return

        for i in range(idx, l):
            candidate.append(s[i])
            self.recur(s, i + 1, cur + 1, k, l, candidate, ans)
            candidate.pop()

test=Solution()
print(test.uniqueSubstring("caaab" , 2))
