# Given a 2D array size of n * m and the elements of each row of the array are sorted. Select 1 number from each row and select n numbers in total. And the diff of n numbers is maximum-minimum, find the minimum diff.
#
# Example
# Input: [[1,2,3,4,5],[6,7,8,9,10]]
# Output: 1
import sys
import heapq


class Solution:
    """
    @param array: a 2D array
    @return: the minimum difference
    """

    def minimumDifference(self, array):
        # Write your code here
        n = len(array)
        if n < 1:
            return -1
        m = len(array[0])
        if m == 0:
            return -1
        hq = []
        curMax = -sys.maxsize
        for i in range(n):
            heapq.heappush(hq, (array[i][0], i, 0))
            curMax = max(curMax, array[i][0])
        ans = sys.maxsize
        while hq:
            curMin, i, j = heapq.heappop(hq)
            ans = min(ans, curMax - curMin)
            if j==m-1:
                break

            temp = array[i][j + 1]
            curMax = max(curMax, temp)
            heapq.heappush(hq, (temp, i, j + 1))

        return ans

arr=[[1,2,3,4,5],[6,7,8,9,10]]
test=Solution()
print(test.minimumDifference(arr))
