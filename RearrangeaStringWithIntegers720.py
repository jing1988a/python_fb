class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """
    def rearrange(self, s):
        # Write your code here
        s=list(s)
        s.sort()
        i=0
        l=len(s)
        if l==0:
            return ""
        total=0
        while i<l:
            if not s[i].isdigit():
                break
            total+=int(s[i])
            i+=1

        return ''.join(s[i:]+[str(total)])