# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# Example
# Example 1:
#
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.
# Example 3:
#
# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
# Notice
# · A word is defined as a character sequence consisting of non-space characters only.
# · Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# · The input array words contains at least one word.
#
#


class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        # write your code here
        l=len(words)
        if l==0:
            return []
        if len(words[0])>maxWidth:
            raise Exception('Invalid input')
        i=1
        cur=[words[0]]
        curLen=len(words[0])
        ans=[]
        while i<l:
            if len(words[i])>maxWidth:
                raise Exception('Invalid input')
            if 1+len(words[i])+curLen<=maxWidth:
                curLen+=1+len(words[i])
                cur.append(words[i])
            else:
                ans.append(self.myFormat(cur , maxWidth))
                cur=[words[i]]
                curLen=len(words[i])

            i+=1
        ans.append(' '.join(cur).ljust(maxWidth))
        return ans

    def myFormat(self , cur , maxWidth):
        l=len(cur)
        space=l-1
        if l==1:
            return cur[0].ljust(maxWidth)
        totalLen=0
        for c in cur:
            totalLen+=len(c)
        totalSpaceNeed=maxWidth-totalLen
        avgSpace=totalSpaceNeed//space
        extraSpace=totalSpaceNeed%space
        res=[cur[0]]
        i=1
        while i<l:
            res.append(" "*avgSpace)
            if extraSpace!=0:
                res.append(" ")
                extraSpace-=1
            res.append(cur[i])
            i+=1
        return ''.join(res)



