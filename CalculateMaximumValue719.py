class Solution:
    """
    @param str: the given string
    @return: the maximum value
    """
    def calcMaxValue(self, str):
        # write your code here
        l=len(str)
        cur=0
        i=0
        while i<l:
            candi=int(str[i])
            if cur*candi<cur+candi:
                cur+=candi
            else:
                cur*=candi
            i+=1
        return cur