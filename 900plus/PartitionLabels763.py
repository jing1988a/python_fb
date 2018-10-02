# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# Seen this question in a real interview before?
# Difficulty:Medium
# Total Accepted:24.4K
# Total Submissions:37.3K
# Contributor:awice
# Subscribe to see which companies asked this question.
#
# Related Topics
#
# Similar Questions
# Merge Intervals
# Python3
#
#
class Solution:
    def partitionLabels(self, S):

        """

        :type S: str

        :rtype: List[int]

        """
        l = len(S)
        cIdx = dict()
        for i in range(l - 1, -1, -1):
            if not S[i] in cIdx:
                cIdx[S[i]] = i
        i = 0
        ans = []
        maxReach = 0
        while i < l:
            maxReach = max(maxReach, cIdx[S[i]])
            j = i
            while j < maxReach:
                maxReach = max(maxReach, cIdx[S[j]])
                j += 1
            ans.append(j - i + 1)
            i = j + 1
        return ans
