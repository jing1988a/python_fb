# Description
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# Have you met this question in a real interview?
# Example
# Gieve s = lintcode,
# dict = ["de", "ding", "co", "code", "lint"].
#
# A solution is ["lint code", "lint co de"].
#
# Related Problems

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        ans=[]
        self.recur(s  , wordDict , [] , ans)
        return ans
    def recur(self ,  s , wordDict , candidate , ans):
        if not s:
            ans.append(' '.join(candidate))
            return
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                candidate.append(s[:i+1])
                self.recur(s[i+1:] , wordDict , candidate , ans)
                candidate.pop()

























