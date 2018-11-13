# Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).
#
# Example
# Given x = 123, return 321
#
# Given x = -123, return -321


class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        flag=1
        if n<0:
            flag=-1
            n=-n
        # return int(str(n)[::-1])*flag

        ans=0
        while n:
            ans=ans*10+n%10
            n//=10
        return ans*flag