# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# Example
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
#
# Return
#
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Notice
# All words have the same length.
# All words contain only lowercase alphabetic characters.


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        if start==end:
            return [start]
        d=set(dict)
        if start in d:
            d.remove(start)
        d.add(end)
        q=[[start , [start]]]
        ans=[]
        found=False
        while q and not found:
            p=[]
            toRemove=set()
            for cur , candidate in q:
                if cur==end:
                    found=True
                    ans.append(candidate[::])

                if not found:
                    for i in range(len(cur)):
                        for c in 'qwertyuiopasdfghjklzxcvbnm':
                            temp=cur[:i]+c+cur[i+1:]
                            if temp in d:
                                toRemove.add(temp)
                                p.append([temp , candidate+[temp]])
            for v in toRemove:
                d.remove(v)
            q=p

        return ans

test=Solution()
print(test.findLadders("hit" , "cog" , ["hot","dot","dog","lot","log"]))



