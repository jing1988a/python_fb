# Description
# Give two users' ordered online time series, and each section records the user's login time point x and offline time point y. Find out the time periods when both users are online at the same time, and output in ascending order.
#
# We guarantee that the length of online time series meet 1 <= len <= 1e6.
# For a user's online time series, any two of its sections do not intersect.
# Have you met this question in a real interview?
# Example
# Given seqA = [(1,2),(5,100)], seqB = [(1,6)], return [(1,2),(5,6)].
#
# Explanation:
# In these two time periods (1,2),(5,6), both users are online at the same time.
# Given seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)], return [].
#
# Explanation:
# There is no time period, both users are online at the same time.
# Related Problems


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import collections
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """

    class Solution:
        """
        @param seqA: the list of intervals
        @param seqB: the list of intervals
        @return: the time periods
        """

        def timeIntersection(self, seqA, seqB):
            d = collections.defaultdict(int)
            for s in seqA:
                d[s.start] += 1
                d[s.end] -= 1
            for s in seqB:
                d[s.start] += 1
                d[s.end] -= 1
            print(d)
            ans = []
            cur = 0
            start = None
            for k in sorted(d.keys()):
                cur += d[k]
                if cur == 2:
                    start = k
                elif cur == 1:
                    if not start is None:
                        ans.append(Interval(start, k))
                        start = None
            return ans

        def timeIntersection2(self, seqA, seqB):
            # Write your code here
            ans = []
            i = j = 0;
            la = len(seqA)
            if la == 0:
                return seqB
            lb = len(seqB)
            if lb == 0:
                return seqA
            ans = []
            while i < la and j < lb:
                if seqA[i].start >= seqB[j].end:
                    j += 1
                elif seqA[i].end <= seqB[j].start:
                    i += 1
                else:
                    ans.append(self.merge(seqA[i], seqB[j]))
                    if seqB[j].end > seqA[i].end:
                        i += 1
                    else:
                        j += 1
            return ans

        def merge(self, a, b):
            start = max(a.start, b.start)
            end = min(a.end, b.end)
            return Interval(start, end)