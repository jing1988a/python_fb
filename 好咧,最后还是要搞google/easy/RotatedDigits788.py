# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].
# Accepted
# 20,755
# Submissions
# 39,518


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans=0
        for i in range(1 , N+1):
            if self.isValid(i):
                ans+=1
        return ans
    def isValid(self , i):
        keyNumCount=0
        for c in str(i):
            if c in ['3' , '4' , '7' ]:
                return False
            if c in ['2' , '5' , '6' , '9']:
                keyNumCount+=1
        return keyNumCount>0