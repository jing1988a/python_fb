# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
#
# Example
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf"
#
# Given the following words in dictionary,
#
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
#
# Notice
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return the smallest in lexicographical order


import collections

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        # Write your code here
        if len(words) == 0:
            return []

        graph, degree = self.constructGraph(words)
        q = []
        for c in degree:
            if degree[c] == 0:
                q.append(c)
        ans = []
        hasMore = True
        while q and hasMore:
            p = []
            hasMore = False
            for node in q:
                ans.append(node)
                for child in graph[node]:
                    degree[child] -= 1
                    if degree[child] == 0:
                        p.append(child)
                        hasMore = True
            if not hasMore:
                break
            q = p
        return ''.join(ans) if len(ans)==len(degree) else []

    def constructGraph(self, words):
        graph = collections.defaultdict(set)
        degree = collections.defaultdict(int)
        for i in range(len(words)):
            for c in words[i]:
                degree[c] = 0
        for i in range(1, len(words)):
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i][j] != words[i - 1][j]:
                    if not words[i][j] in graph[words[i - 1][j]]:
                        graph[words[i - 1][j]].add(words[i][j])
                        degree[words[i][j]] += 1
                    break
        return graph, degree


a=["za","zb","ca","cb"]
test=Solution()
print(test.alienOrder(a))

