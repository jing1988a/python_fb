# Given a string containing n lowercase letters, the string needs to divide into several substrings, the letter in the substring should be same, and the number of letters in the substring does not exceed k, and output the minimal substring number meeting the requirement.
#
# Example
# Give s = "aabbbc", k = 2, return 4
#
# Explaination:
# we can get "aa", "bb", "b", "c" four substring.
# Give s = "aabbbc", k = 3, return 3
#
# Explaination:
# we can get "aa", "bbb", "c" three substring.
# Notice
# n \leq 1e5n≤1e5


class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """

    def getAns(self, s, k):
        # Write your code here
        l = len(s)
        if l < k:
            return 0
        if k < 1:
            return -1
        cur = 1
        ans = 0
        pre = s[0]
        i = 1
        while i < l:
            if cur == k:
                ans += 1
                pre = s[i]
                cur = 1
            else:
                if s[i] == pre:
                    cur += 1
                else:
                    ans += 1
                    pre = s[i]
                    cur = 1
            i += 1

        return ans+1
