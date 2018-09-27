class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        # l1=len(s1)
        # l2=len(s2)
        # l3=len(s3)
        # if l3!=l1+l2:
        #     return False
        # i=j=k=0
        # while k<l3:
        #     if i<l1 and s3[k]==s1[i]:
        #         k+=1
        #         i+=1
        #     elif j<l2 and s3[k]==s2[j]:
        #         k+=1
        #         j+=1
        #     else:
        #         return False
        # return True
        # is greedy correct or is it wrong?? can only pass 94% test case

        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        if l3!=l1+l2:
            return False
        dp=[[False for i in range(l2+1)] for j in range(l1+1) ]
        dp[0][0]=True
        for i in range(1 , l1+1):
            if s3[i-1]==s1[i-1]:
                dp[i][0]=True
        for j in range(1 , l2+1):
            if s3[j-1]==s2[j-1]:
                dp[0][j]=True

        for i in range(1 , l1+1):
            for j in range(1 , l2+1):
                if s3[i+j-1]==s1[i-1] and dp[i-1][j]:
                    dp[i][j]=True
                if s3[i+j-1]==s2[j-1] and dp[i][j-1]:
                    dp[i][j]=True
        return dp[l1][l2]


test=Solution()
print(test.isInterleave("a" ,"" ,"a"))
