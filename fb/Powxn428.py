class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if x==0:
            return 0
        if n<0:
            return 1.0/self.myPow(x , -n)
        if n==0:
            return 1
        temp=self.myPow(x , n//2)
        if n%2==1:
            return temp*temp*x
        else:
            return temp*temp

a=Solution()
a.myPow(3 , 3)