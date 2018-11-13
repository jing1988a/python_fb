# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# Example
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Notice
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end:
            return 1
        d = set(dict)
        if start in d:
            d.remove(start)
        d.add(end)
        q = [[start, 1]]
        ans = 1
        while q:
            p = []
            for cur, candidate in q:
                if cur == end:
                    return candidate
                for i in range(len(cur)):
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        temp = cur[:i] + c + cur[i + 1:]
                        if temp in d:
                            d.remove(temp)
                            p.append([temp, candidate + 1])
            q = p
        return ans
