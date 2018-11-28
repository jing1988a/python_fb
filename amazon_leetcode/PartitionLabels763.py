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




class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l=len(S)
        if l==0:
            return []
        d=dict()
        for i in range(l-1 , -1 , -1):
            if S[i] in d:
                continue
            d[S[i]]=i

        start=0

        ans=[]

        while start<l:
            cur=start
            end = d[S[start]]
            while cur<=end:
                end=max(d[S[cur]] , end)
                cur+=1
            ans.append(end-start+1)
            start=cur
        return ans


test=Solution()
test.partitionLabels("ababcbacadefegdehijhklij")
