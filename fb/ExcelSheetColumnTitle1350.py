class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        ans=[]
        while n!=0:
            cur=(n-1)%26
            ans.append(  chr(cur+ord('A')) )
            n=(n-1)//26
        return ''.join(reversed(ans))