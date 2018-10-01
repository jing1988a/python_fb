class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        ans=[]
        self.recur(0 , [] , n , ans)
        return ans
    def recur(self , idx , candidate , n , ans):
        if idx==n:
            ans.append(self.myFormat(candidate  , n))
        for i in range(n):
            if self.isValid(i , idx , candidate , n):
                candidate.append(i)
                self.recur(idx+1 , candidate , n , ans)
                candidate.pop()

    def isValid(self , v , idx , candidate  , n ):
        i=1
        while idx-i>-1:
            if candidate[idx-i]==v or candidate[idx-i]==v-i or candidate[idx-i]==v+i:
                return False
            i+=1
        return True
    def myFormat(self , candidate  , n):
        ans=[]
        for i in range(n):
            temp=["." for i in range(n)]
            temp[candidate[i]]="Q"
            ans.append(''.join(temp))
        return ans
        
test=Solution()
print(test.solveNQueens(1))