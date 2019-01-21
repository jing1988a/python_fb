# A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.
#
#
#
# Example 1:
#
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# Example 2:
#
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:
#
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#



import sys

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        l=len(S)
        if l<2:
            return 0
        leftOnes=[]
        cur=0
        for i in range(l):
            leftOnes.append(cur)
            if S[i]=='1':
                cur+=1

        rightZeros=[0 for i in range(l)]
        cur=0
        for i in range(l-1 , -1, -1):
            rightZeros[i]=cur
            if S[i]=='0':
                cur+=1
        ans=sys.maxsize
        for i in range(l):
            ans=min(ans , rightZeros[i]+leftOnes[i])
        return ans