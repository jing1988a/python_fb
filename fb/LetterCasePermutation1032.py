class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here
        ans=[]
        l=len(S)
        self.recur(S , 0 , l , [] , ans)
        return ans
    def recur(self , S , start , l , candidate , ans):
        if start==l:
            ans.append(''.join(candidate))
            return
        if S[start].isdigit():
            candidate.append(S[start])
            self.recur(S , start+1 , l , candidate , ans)
        else:
            candidate.append(S[start].lower())
            self.recur(S , start+1 , l , candidate , ans)
            candidate.pop()
            candidate.append(S[start].upper())
            self.recur(S , start+1 , l , candidate , ans)
        candidate.pop()
