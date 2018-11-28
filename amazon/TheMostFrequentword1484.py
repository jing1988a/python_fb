# Give a string s witch represents the content of the novel, and then give a list indicating that the words do not participate in statistics, find the most frequent word(return the one with the smallest lexicographic order if there are more than one word)
#
# Example
# Input: s = "Jimmy has an apple, it is on the table, he like it"
# excludeWords = ["a","an","the"]
# Output:"it"

import collections

class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        excludewords=set(excludewords)
        maxCount=0
        ans=None
        d=collections.defaultdict(int)
        for word in s.split(' '):
            word=word.strip(',')
            word=word.strip('.')
            if word in excludewords:
                continue
            d[word]+=1
            if d[word]>maxCount:
                maxCount=d[word]
                ans=word
            elif d[word]==maxCount and self.isSmaller(word , ans):
                ans=word
        return ans
    def isSmaller(self , a ,  b):
        l1=len(a)
        l2=len(b)
        i=0
        while i<min(l1 , l2):
            if ord(a[i])>ord(b[i]):
                return False
            if ord(a[i])<ord(b[i]):
                return True

            i+=1
        return l1<l2