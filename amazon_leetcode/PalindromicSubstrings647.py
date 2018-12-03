# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.
# Accepted
# 69,892
# Submissions
# 127,703


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        dp=[[0 for i in range(l)] for j in range(l)]
        ans=0
        for i in range(l):
            dp[i][i]=1
            ans+=1
        for i in range(l-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                ans+=1
        for length in range(3 , l+1):
            for start in range(l-length+1):
                end=start+length-1
                if s[start]==s[end] and dp[start+1][end-1]==1:
                    dp[start][end]=1
                    ans+=1
        return ans


