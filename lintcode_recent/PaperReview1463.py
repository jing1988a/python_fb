# We define that the similarity between two papers is the longest similar word subsequence * 2 divided by the total length of two papers.
# Given two papers, words1, words2 (each represented as an array of strings), and a list of similar pairs of words pairs, find the similarity between the two papers.
# Note: Similar relationships are transitive. For example, if "great" is similar to "good" and "find" is similar to "good", then "geat" and "find" are similar.
# Similarity is also symmetrical. For example, "great" is similar to "good" and "good" is similar to "great".
# In addition, a word is always similar to itself.
#
# Example
# Give words1= ["great","acting","skills","life"] ，words2= ["fine","drama","talent","health"] ，pairs= [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]，return 0.75.
#
# Explanation:
# The similar word sequence for the two words is
# `"great","acting","skills"
# "fine","drama","talent"
# The total length is 8.
# The similarity is 6/8=0.75
# Give words1= ["I","love","you"] ，words2= ["you","love","me"] ，pairs= [["I", "me"]]，return 0.33。
#
# Explanation:
# The similar word sequence for the two words is
# "I"
# "me"
# or
# "love"
# "love"
# or
# "you"
# "you"
# The total length is 6.
# The similarity is 2/6=0.33


class Solution:
    """
    @param words1: the words in paper1
    @param words2: the words in paper2
    @param pairs: the similar words pair
    @return: the similarity of the two papers
    """
    def getSimilarity(self, words1, words2, pairs):
        # Write your code here
        u=Union()
        for p in pairs:
            p1=u.findP(p[0])
            p2=u.findP(p[1])
            u.unionP(p1 , p2)
        l=len(words1)
        temp=0
        ans=0
        for i in range(l):
            if u.findP(words1[i])==u.findP(words2[i]):
                temp+=1
                ans=max(ans , temp)
            else:
                temp=0
        return ans/l

class Union:
    def __init__(self):
        self.d=dict()
    def findP(self , v):
        if not v in self.d:
            self.d[v]=v
        if self.d[v]==v:
            return v
        p=self.findP(self.d[v])
        self.d[v]=p
        return p
    def unionP(self , p1 , p2):
        if p1==p2:
            return
        self.d[p1]=p2