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




class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        l=len(words)
        if l<2:
            return sorted(words[0])
        degree,graph=self.constructGraph(words , l)
        q=[]
        for c in degree:
            if degree[c]==0:
                q.append(c)
        ans=[]
        visited=set()
        while q:
            # print()
            # q.sort()
            p=[]
            for c in q:
                ans.append(c)
                visited.add(c)
                for child in  graph[c]:
                    degree[child]-=1
                    if degree[child]==0:
                        p.append(child)
            q=p
        return ''.join(ans) if len(visited)==len(degree) else []
    def constructGraph(self , words , l):
        degree=dict()
        graph=collections.defaultdict(list)
        for i in range(l):
            for c in words[i]:
                if not c in degree:
                    degree[c]=0

        i=1
        while i <l:
            preL=len(words[i-1])
            curL=len(words[i])
            j=0
            while j<min(preL , curL):
                if words[i-1][j]!=words[i][j]:
                    degree[words[i][j]]+=1
                    graph[words[i-1][j]].append(words[i][j])
                    break
                j+=1
            i+=1
        return degree , graph