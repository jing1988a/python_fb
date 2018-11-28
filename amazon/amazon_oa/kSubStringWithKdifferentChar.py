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
        l = len(stringIn)
        if l<K:
            return 0
        d=collections.defaultdict(int)
        for i in range(K):
            d[stringIn[i]]+=1
        #ans=0
        total=set()
        if len(d)==K:
            #ans+=1
            total.add(stringIn[:K])
        start=0
        end=K
        while end<l:
            d[stringIn[end]]+=1
            d[stringIn[start]]-=1
            if d[stringIn[start]]==0:
                del d[stringIn[start]]
            if len(d)==K:
                #ans+=1
                total.add(stringIn[start+1:end+1])
            start+=1
            end+=1
        #return ans
        return len(total)



# acutally this is question is very straightward to come up with an idea
# basicly we keep track a substring of length K and keep moving from left all
# the way to the right like a sliding window. the tricky part is the hidden test case.
# i'm not sure but based on the test case, it seems substring has the same value but diffrernt start and end index is
# considered as same string.