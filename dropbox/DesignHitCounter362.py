# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?


# 1 using a queue, everytime hit , check front and delete those with timestamp more than 5 min
# 2 will there be more than 1 hit at the same timestamp?
import time


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[[None , None] for _ in range(300)]



    def hit(self, timestamp=None):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        timestamp=time.time()
        idx=timestamp%300
        if self.queue[idx][0] is not None:
            if self.queue[idx][0]!=timestamp:
                self.queue[idx]=[timestamp , 1]
            else:
                self.queue[idx][1] +=1
        else:
            self.queue[idx] = [timestamp, 1]



    def getHits(self, timestamp=None):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        timestamp = time.time()
        print(timestamp)
        result=0
        for timestampHistory , hit in self.queue:
            if timestampHistory and timestamp-timestampHistory<300:
                result+=hit
        return result




