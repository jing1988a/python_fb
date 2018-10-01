class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        if not s:
            return [""]
        visited=set()
        q=[s]
        find=False
        ans=[]
        while q:
            p=[]
            for cur in q:
                for i in range(len(cur)):
                    if cur[i] in [")" , "("]:
                        nextStr=cur[:i]+cur[i+1:]
                        if not nextStr in visited:
                            visited.add(nextStr)
                            p.append(nextStr)
                            if self.isValid(nextStr):
                                find=True
                                ans.append(nextStr)
            if find:
                break
            q=p
        return ans
    def isValid(self , s):
        count=0
        for c in s:
            if c=="(":
                count+=1
            elif c==")":
                count-=1
            if count<0:
                return False
        return count==0