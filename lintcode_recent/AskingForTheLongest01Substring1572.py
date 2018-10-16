# 1572. Asking For The Longest 01 Substring
# Now that there is a 01 string str, your task is to find the longest 01 consecutive substrings, with 0 and 1 alternating, for example 010, 10101, 01. However, this is a simple problem for the excellent lintcode students. So now, you can do something to make 01 consecutive substrings as long as possible. The operation means that you can select a position, break the string, turn it into two strings, then flip each string and finally stitch them together in the original order. You can do this zero or more times and return the length of the largest 01 consecutive substring you can finally get.
#
# Example
# Give str="100010010" and return 5.
#
# You can split 10|0010010 , and after flipping on both sides, it becomes 01|0100100.
# That is, 010100100, select position 1 to position 5, 01010, and the length is 5.
# Give str="1001" and return 2.
#
# No matter how you split the flip, it won't make the answer bigger. So 10 is the largest 01 consecutive substring and returns 2.
# Notice
# String length does not exceed 100000



class Solution:
    """
    @param str: the string
    @return: the length of substring
    """
    def askingForTheLongest01Substring(self, strs):
        # Write your code here
        l=len(strs)
        if l==0:
            return 0
        s=strs+strs
        dp=[0 for i in range(2*l)]
        dp[0]=1
        ans=1
        for i in range(1 , 2*l):
            if s[i]!=s[i-1]:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=1
            if dp[i]==l:
                return l
            ans=max(ans , dp[i])
        return ans