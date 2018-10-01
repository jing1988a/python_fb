class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        cCount=collections.Counter(tasks)
        l=len(tasks)
        maxCount=0
        for c in cCount:
            if cCount[c]>maxCount:
                maxCount=cCount[c]
        totalMaxC=0
        for c in cCount:
            if cCount[c]==maxCount:
                totalMaxC+=1
        return max(l , (maxCount-1)*(n+1)+totalMaxC)

