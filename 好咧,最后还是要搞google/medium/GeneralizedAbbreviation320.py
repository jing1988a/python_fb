# Write a function to generate the generalized abbreviations of a word.
#
# Note: The order of the output does not matter.
#
# Example:
#
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]



class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ans=[]
        l=len(word)
        self.recurBuild(0 ,  l , []  , word  , ans)
        return ans
    def recurBuild(self , idx , l , candidate , word , ans):
        if idx==l:
            candidate=map(str , candidate)
            ans.append(''.join(candidate))
            return
        #option 1, keep this c
        candidate.append(word[idx])
        self.recurBuild(idx+1 , l ,  candidate , word , ans)
        candidate.pop()
        #option 2, change this c
        if not candidate or  type(candidate[-1])!=int:
            candidate.append(1)
            self.recurBuild(idx+1 , l ,  candidate , word , ans)
            candidate.pop()

        else:
            candidate[-1]+=1
            self.recurBuild(idx+1 , l ,  candidate , word , ans)
            candidate[-1]-=1



