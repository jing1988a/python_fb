# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# Example
# Given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
#


class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        ans=[]
        self.recur(n , n , [] , ans)
        return ans
    def recur(self , l , r , candidate , ans):

        if l==r==0:
            ans.append(''.join(candidate))
            return
        if l>r:
            return
        if l>0:
            candidate.append('(')
            self.recur(l-1 , r , candidate , ans)
            candidate.pop()
        if r>0:
            candidate.append(')')
            self.recur(l , r-1 , candidate  , ans)
            candidate.pop()


test=Solution()
print(test.generateParenthesis(1))