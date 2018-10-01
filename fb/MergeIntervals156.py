"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        l=len(intervals)
        if l<2:
            return intervals
        intervals.sort(key=lambda x:x.start)
        s=intervals[0].start
        e=intervals[0].end
        res=[]
        i=1
        while i<l:
            if intervals[i].start<=e:
                e=max(e , intervals[i].end)
            else:
                res.append(Interval(s , e))
                s=intervals[i].start
                e=intervals[i].end
            i+=1
        res.append(Interval(s , e))
        # print(res)
        return res