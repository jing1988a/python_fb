# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#
# Example 1:
#
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# Example 2:
#
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# Example 3:
#
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false

class Solution:
    # def __init__(self):
    #     self.foundMatch=None
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = len(str)
        dic = dict()
        usedWords = set()
        return self.recurCheck(pattern, 0, str, 0, dic, usedWords)

    def recurCheck(self, pattern, pIdx, s, sIdx, dic, usedWords):
        if pIdx == len(pattern) and sIdx == len(s):
            return True
        if pIdx == len(pattern) or sIdx == len(s):
            return False
        candidatePattern = pattern[pIdx]
        for i in range(sIdx, len(s)):
            temp = s[sIdx:i + 1]
            if candidatePattern in dic:
                if temp == dic[candidatePattern]:
                    if self.recurCheck(pattern, pIdx + 1, s, i + 1, dic, usedWords):
                        return True
            else:
                if temp in usedWords:
                    continue
                dic[candidatePattern] = temp
                usedWords.add(temp)
                if self.recurCheck(pattern, pIdx + 1, s, i + 1, dic, usedWords):
                    return True
                del dic[candidatePattern]
                usedWords.remove(temp)
        return False
