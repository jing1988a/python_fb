# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
#
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
#
import heapq


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        hq = []
        for k, v in enumerate(nums):
            heapq.heappush(hq, [-v, k])
        ans=[None for i in range(len(nums))]
        i=1
        while hq:
            v , k =heapq.heappop(hq)
            if i==1:
                ans[k]="Gold Medal"
            elif i==2:
                ans[k] = "Silver Medal"
            elif i==3:
                ans[k] = "Bronze Medal"
            else:
                ans[k]=str(i)
            i+=1
        return ans


