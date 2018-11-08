# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)
#
# Example
# Given pattern = "abab", str = "redblueredblue", return true.
# Given pattern = "aaaa", str = "asdasdasdasd", return true.
# Given pattern = "aabb", str = "xyzabcxzyabc", return false.
#
# Notice
# You may assume both pattern and str contains only lowercase letters.



class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """


    def wordPatternMatch(self, pattern, s):
        # write your code here
        return self.isMatch(pattern , s , dict() , set())
    def isMatch(self , pattern , s , d , used):
        if not pattern:
            if not s:
                return True
            return False
        if pattern[0] in d:
            if not s.startswith(d[pattern[0]]):
                return False
            return self.isMatch(pattern[1:] , s[len(d[pattern[0]]):] , d , used )
        for i in range(len(s)):
            if s[:i+1] in used:
                continue
            used.add(s[:i+1])
            d[pattern[0]]=s[:i+1]
            if self.isMatch(pattern[1:] , s[len(d[pattern[0]]):] , d , used ):
                return True

            del d[pattern[0]]
            used.remove(s[:i+1])
        return False






pattern = "abab"
s = "redblueredblue"
test=Solution()
print(test.wordPatternMatch(pattern , s))
























