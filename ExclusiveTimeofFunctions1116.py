class Solution:
    """
    @param n: a integer
    @param logs: a list of integers
    @return: return a list of integers
    """

    # ans[6 , 4 , 5 , 6]
    # ["0:start:0",
    #  "1:start:2",
    #  "1:end:5",
    #   2:start:10,
    #   3:start:15,
    #   3:end:20,
    #   2:end:25
    #  "0:end:60"]
    # Output:[3, 4]
    def exclusiveTime(self, n, logs):
        # write your code here
        ans = [0 for i in range(n)]
        stack = []
        curTime = 0
        for temp in logs:
            pId, action, timeStamp = temp.split(":")
            timeStamp=int(timeStamp)
            if action == 'start':
                if stack:
                    preId = stack[-1]
                    ans[preId] += timeStamp - curTime
                curTime = timeStamp
                stack.append(int(pId))
            else:
                preId = stack.pop()
                ans[preId] += timeStamp - curTime + 1
                curTime = timeStamp + 1
        return ans


tset = Solution()
print(tset.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))
