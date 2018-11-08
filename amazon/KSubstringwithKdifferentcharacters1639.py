# Given a string S and an integer K.
# Calculate the number of substrings of length K and containing K different characters
#
# Example
# String: "abcabc"
# K: 3
#
# Answer: 3
# substrings:  ["abc", "bca", "cab"]
# String: "abacab"
# K: 3
#
# Answer: 2
# substrings: ["bac", "cab"]
import collections
class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        total=set()
        l=len(stringIn)
        if l<K:
            return 0
        d=collections.defaultdict(int)
        for i in range(K):
            d[stringIn[i]]+=1
        if len(d)==K:
            total.add(stringIn[:K])
        print(d)
        start=0
        end=K
        while end<l:
            d[stringIn[start]]-=1
            d[stringIn[end]]+=1
            if d[stringIn[start]]==0:
                del d[stringIn[start]]
            print(d)
            if len(d) == K:
                total.add(stringIn[start:start+K])
            start+=1
            end+=1
        return len(total)

s="abcabc"
k=3
test=Solution()
print(test.KSubstring(s , k))

