# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
#
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Note:
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l=len(S)
        S=list(S)
        s=0
        e=l-1
        while s<e:
            if not S[s].isalpha():
                s+=1
            elif not  S[e].isalpha():
                e-=1
            else:
                S[s] , S[e]=S[e] , S[s]
                s+=1
                e-=1
        return ''.join(S)
