class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
        return len(s.strip().split(' ')[-1])