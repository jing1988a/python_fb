class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        # Write your code here
        start=0
        end=len(s)-1
        while start<end:
            if s[start]!=s[end]:
                return self.isPalin(s[:start]+s[start+1:]) or self.isPalin(s[:end]+s[end+1:])
            start+=1
            end-=1
        return True
    def isPalin(self , s):
        start=0
        end=len(s)-1
        while start<end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True