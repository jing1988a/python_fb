# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].
import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counts=collections.Counter(S)
        maxCount=max(counts.values())
        l=len(S)
        temp=[]
        ans=[None]*l
        if l%2==0 and maxCount>=l//2+1:
            return ""
        if l%2==1 and maxCount>l//2+1:
            return ""

        for k in counts:
            if counts[k]==maxCount:
                temp+=[k for _ in range(maxCount)]
                del counts[k]
                break
        for k in counts:
            temp+=[k for _ in range(counts[k])]
        if l%2==0:
            ans[::2], ans[1::2] = temp[:l//2], temp[l//2:]
        else:

            ans[::2], ans[1::2] = temp[:l//2+1], temp[l//2+1:]
        return ''.join(ans)