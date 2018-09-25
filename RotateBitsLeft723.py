class Solution:
    """
    @param n: a number
    @param d: digit needed to be rorated
    @return: a number
    """
    def leftRotate(self, n, d):
        # write code here
        a=(bin(n)[2:]).zfill(32)
        temp=a[d:]+a[:d]
        ans=0
        for i in range(len(temp)):
            ans=ans*2+int(temp[i])
        return ans