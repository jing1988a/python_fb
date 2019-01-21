# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true

import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter=collections.Counter(s)
        oddCount=0
        for c in counter:
            if counter[c]%2!=0:
                oddCount+=1
                if oddCount>1:
                    return False
        return True