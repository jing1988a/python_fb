# Give k, a, b, which means a and b are all k base numbers, and output a + b.
#
# Example
# Given k = 3, a = "12", b = "1", return "20".
#
# Explanation:
# 12 + 1 = 20 in 3 bases.
# Given k = 10, a = "12", b = "1", return "13".
#
# Explanation:
# 12 + 1 = 13 in 10 bases.
# Notice
# 2 <= k <= 10
# a, b are strings, the length does not exceed 1000.
# There may be a leading zero.


class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        # Write your code here
        a=list(a.lstrip("0"))
        b=list(b.lstrip("0"))
        a.reverse()
        b.reverse()
        l1=len(a)
        l2=len(b)
        i=0
        temp=0
        ans=[]
        while temp or i<max(l1 , l2):
            if i<l1:
                temp+=int(a[i])
            if i<l2:
                temp+=int(b[i])
            ans.append(str(temp%k))
            temp//=k
            i+=1
        return ''.join(reversed(ans))