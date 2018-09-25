class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """
    def hIndex(self, citations):
        # write your code here
        n=len(citations)
        dp=[0 for i in range(n+1)]
        for c in citations:
            if c>=n:
                dp[n]+=1
            else:
                dp[c]+=1
        ans=0
        i=n
        while i>-1:
            ans+=dp[i]
            if ans>=i:
                break
            i-=1
        return i