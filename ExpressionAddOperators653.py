class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def __init__(self):
        self.ans=[]
    def addOperators(self, num, target):
        # write your code here
        self.recur(num , 1 , "" , target )
        return self.ans
    def recur(self , lStr , rNum , rStr , target):

        if not self.leadingZero(lStr) and int(lStr)*rNum==target:
            self.ans.append(lStr+rStr)
        for i in range(1 , len(lStr)):
            newLStr=lStr[:i]
            newRStr=lStr[i:]
            if self.leadingZero(newRStr):
                continue
            newRNum=int(newRStr)*rNum
            newRStr=newRStr+rStr
            self.recur(newLStr , newRNum , "*"+newRStr , target)
            self.recur(newLStr , 1 , "-"+newRStr , target+newRNum)
            self.recur(newLStr , 1 , "+"+newRStr , target-newRNum)


    def leadingZero(self , s):
        return len(s)>1 and s[0]=='0'

test=Solution()
print(test.addOperators("123" , 6))