# Given a string S containing only uppercase letters, insert as few '_' as possible in S so that the distance of same kind of letters no less than k, and if there are multiple solutions,just make the lexicographical order of the target string as small as possible. For example, given S = ”AABACCDCD”, k = 3, the target string is “A__AB_AC__CD_CD”. Since the length of target string may be very long, we only need to return the number of '_' inserted before each position of the original string. For example, the previous example returns [0,2,0,1,0,2,0,1,0].
# (The lexicographical order of '_' is greater than'Z')
#
# Example
# GivenS="AABACCDCD",k = 3,return [0,2,0,1,0,2,0,1,0]
#
# Explanation：
# The target string is "A__AB_AC__CD_CD"
# GivenS = "ABBA",k = 2,return[0,0,1,0]
#
# Explanation：
# The target string is”AB_BA”

class Solution:
    """
    @param k: The necessary distance of same kind of letters
    @param S: The original string
    @return: Return the number of '_' inserted before each position of the original string
    """
    def getAns(self, k, S):
        # Write your code here.
        d=dict()
        ans=[]
        l=len(S)
        for i in range(l):
            preIdx=d.get(S[i] , -sys.maxsize)
            temp=max(0 , k-(i-preIdx))
            if temp>0:
                for c in d:
                    d[c]-=temp
            ans.append(temp)
            d[S[i]]=i
        return ans
