"""
Definition of Interval.

"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        l=len(intervals)
        if l<2:
            return True
        intervals.sort(key=lambda x : x.start)
        end=intervals[0].end
        for i in range(1 , l):
            if intervals[i].start<end:
                return False
            end=intervals[i].end
        return True


a=Interval(5 , 8)
b=Interval(6 , 8)
test=Solution()
print(test.canAttendMeetings([a , b]))