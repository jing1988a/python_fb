# Given some intervals, ask how many are covered most, if there are multiple, output the smallest number.
#
# Example
# Given intervals = [(1,7),(2,8)], return 2.
#
# Explanation:
# 2 is covered 2 times, and is the number of 2 times the smallest number.
# Given intervals = [(1,3),(2,3),(3,4)], return 3.
#
# Explanation:
# 3 is covered 3 times.
# Notice
# the number of the interval is not more than 10^5.
# the left and right endpoints of the interval are greater than 0 not more than 10^5.




"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        d=dict()
        for i in intervals:
            s=i.start
            e=i.end
            if s in d:
                d[s][0]+=1
            else:
                d[s]=[1  , 0]

            if e in d:
                d[e][1]+=1
            else:
                d[e]=[0 , 1]
        curMax=0
        ans=None
        temp=0
        for k in sorted(d.keys()):
            temp+=d[k][0]
            if curMax<temp:
                curMax=temp
                ans=k
            temp-=d[k][1]
        return ans