# Given a digit string excluded 01, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# Cellphone
#
# Example
# Given "23"
#
# Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# Notice
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        d = dict()
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        ans=[]
        self.recur(digits , 0 , ans , [] , d)
        return ans
    def recur(self , digits , i , ans , candidate , d):
        if i==len(digits):
            ans.append(''.join(candidate))
            return
        if not digits[i] in d:
            raise Exception('invald input')
        for v in d[digits[i]]:
            candidate.append(v)
            self.recur(i+1 , ans , candidate , d)
            candidate.pop()






















