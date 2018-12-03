# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=len(s)
        if l==0:
            return True
        a=[]
        b=[]
        for i in l:
            if s[i]=='(':
                a.append(i)
            if s[i]=='*':
                b.append(i)
            if s[i]==')':
                if a:
                    a.pop()
                elif b:
                    b.pop()
                else:
                    return False
        while a :
            if not b or a[-1]>b[-1]:
                return False
            a.pop()
            b.pop()
        return True
