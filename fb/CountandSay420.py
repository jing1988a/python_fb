class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def countAndSay(self, n):
        # write your code here
        if n==1:
            return "1"
        i=1;
        res="1"
        while i<n:
            ans=[]
            count=0
            pre=None
            for c in res:
                if c!=pre:
                    if pre is not None:
                        ans.append(str(count))
                        ans.append(pre)
                    count=1
                else:
                    count+=1
                pre=c
            ans.append(str(count))
            ans.append(pre)
            res=ans
            i+=1
        return ''.join(res)