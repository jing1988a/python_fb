# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.
#
# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
# Accepted
# 19,568
# Submissions
# 46,302

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1)!=len(words2):
            return False
        u=Union()
        for x , y in pairs:
            p1=u.findP(x)
            p2=u.findP(y)
            if p1!=p2:
                u.union(p1 , p2)
        for w1 , w2  in zip(words1 , words2):
            p1=u.findP(w1)
            p2=u.findP(w2)
            if p1!=p2:
                return False
        return True

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
    def union(self, p1 , p2):
        if p1==p2:
            return
        self.d[p1]=p2
