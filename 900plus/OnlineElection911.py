# In an election, the i-th vote was cast for persons[i] at time times[i].
#
# Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.
#
# Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.
#
#
#
# Example 1:
#
# Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation:
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
#
#
# Note:
#
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
import bisect
import collections

# a = [1, 1, 3, 4, 4, 4]
# print(bisect.bisect_right(a, 4))


class TopVotedCandidate:
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        curMax = 0
        curV = None
        self.d = collections.OrderedDict()
        self.count = collections.defaultdict(int)
        for i in range(len(persons)):
            k = persons[i]
            v = self.count[k] + 1
            self.count[k] = v
            if v >= curMax:
                curV = persons[i]
                curMax = v
            self.d[times[i]] = curV
        self.keys = list(self.d.keys())
        # print(self.d)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        latestTime = 0
        if t in self.d:
            latestTime = t
        else:
            floorKey = bisect.bisect(self.keys, t) - 1
            if floorKey == -1:
                return None

            latestTime = self.keys[floorKey]
            # print(latestTime)

        return self.d[latestTime]

test = TopVotedCandidate([0,1,1,0,0,1,0], [0,5,10,15,20,25,30])
print(test.q(3))
print(test.q(12))
print(test.q(25))
print(test.q(15))
print(test.q(24))
print(test.q(8))

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# Input:
# ["TopVotedCandidate","q","q","q","q","q","q"]
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output:
# [null,0,0,1,0,1,0]
# Expected:
# [null,0,1,1,0,0,1]