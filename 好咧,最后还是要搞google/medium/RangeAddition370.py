# Assume you have an array of length n initialized with all 0's and are given k update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]
# Explanation:
#
# Initial state:
# [0,0,0,0,0]
#
# After applying operation [1,3,2]:
# [0,2,2,2,0]
#
# After applying operation [2,4,3]:
# [0,2,5,5,3]
#
# After applying operation [0,2,-2]:
# [-2,0,3,5,3]

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        idxActions = []
        for update in updates:
            idxActions.append([update[0], update[2]])
            idxActions.append([update[1] + 1, -update[2]])
        idxActions.sort(key=lambda x: x[0])
        cur = 0
        d = dict()
        for idx, action in idxActions:
            cur += action
            d[idx] = cur
        ans = [0 for i in range(length)]
        cur = 0
        val = 0
        print(d)
        for idx in sorted(d.keys()):
            for i in range(cur, idx):
                ans[i] = val
            val = d[idx]
            cur = idx
        for i in range(cur, length):
            ans[i] = val
        return ans

    # 这个可以优化的,  下面这个可以写进一个for loop 里

    # for idx, action in idxActions:
    #     cur += action
    #     d[idx] = cur
    # ans = [0 for i in range(length)]
    # cur = 0
    # val = 0
    # print(d)
    # for idx in sorted(d.keys()):
    #     for i in range(cur, idx):
    #         ans[i] = val
    #     val = d[idx]
    #     cur = idx
