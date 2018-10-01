class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        # dp[i]= max at index i
        l=len(A)
        if l==0:
            return None
        curMax=A[0]
        curI=0
        curJ=0
        dp=[ [None , None] for i in range(l) ]
        dp[0]=[A[0] , 0]

        i=1
        while i<l:
            if dp[i-1][0]<0:
                dp[i]=[A[i] , i]
            else:
                dp[i]=[A[i]+dp[i-1][0] , dp[i-1][1]  ]
            if curMax<dp[i][0]:
                curMax=dp[i][0]
                curI=dp[i][1]
                curJ=i
            i+=1
        return [curI , curJ]

test=Solution()
print(test.continuousSubarraySum([-101,-33,-44,-55,-67,-78,-101,-33,-44,-55,-67,-78,-100,-200,-1000,-22,-100,-200,-1000,-22]))