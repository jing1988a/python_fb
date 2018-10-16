#
# 1465. Order Of Tasks
# There are n different tasks, the execution time of tasks are t[], and the probability of success are p[]. When a task is completed or all tasks fail, the operation ends. Tasks are performed in a different order, and it is expected that the time to stop the action is generally different. Please answer in what order to perform the task in order to make the end of the expected action the shortest time? If the expected end time of the two task sequences is the same, the lexicographic minimum order of tasks is returned.
#
# Example
# Given n=1, t=[1], p=[1.0], return [1].
#
#
# Explanation:
# The shortest expected action end time is 1.0*1+(1.0-1.0)*1=1.0
#
# Given n=2, t=[1,2], p=[0.3, 0.7], return [2,1].
#
#
# Explanation:
# The shortest expected action end time is 0.7*2+(1.0-0.7)*0.3*(2+1)+(1.0-0.7)*(1.0-0.3)*(2+1)=2.3

class Solution:
    """
    @param n: The number of tasks
    @param t: The time array t
    @param p: The probability array p
    @return: Return the order
    """
    def getOrder(self, n, t, p):
        # Write your code here
        if n==0:
            return []
        ans=[]
        temp=[]
        for i in range(n):
            if p[i]==0:
                temp.append([sys.maxsize , i])
            else:
                temp.append([t[i]/p[i] , i])
        temp.sort()
        for i in range(n):
            ans.append(temp[i][1]+1)
        return ans