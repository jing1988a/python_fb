class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here

        num=list(str(num))
        l=len(num)
        i=l-1
        if i<1:
            return int(''.join(num))
        dp=[[None,None] for _ in range(i+1)]
        curMax=0
        curL=l-1
        while i >-1:
            dp[i]=[curMax , curL]
            if curMax<int(num[i]):
                curMax=int(num[i])
                curL=i
            i-=1
        for i in range(l ):
            if dp[i][0]>int(num[i]):
                num[i] , num[dp[i][1]]=num[dp[i][1]] ,num[i]
                break

        return int(''.join(num))

test=Solution()
print(test.maximumSwap(0))