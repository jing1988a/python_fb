class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        ans=[]
        count=0
        i=0
        l=len(s)
        candi=[]
        while i<l:
            if s[i].isdigit():
                count=count*10+int(s[i])
            elif s[i]=="[":
                c=1
                j=i
                while c!=0:
                    j+=1
                    if s[j]=="[":
                        c+=1
                    elif s[j]=="]":
                        c-=1
                ans+=self.expressionExpand(s[i+1:j])*count
                count=0
                i=j
            else:
                ans.append(s[i])
            i+=1
        return ''.join(ans)