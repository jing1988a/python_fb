class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def countArrangement(self, N):
        # Write your code here
        visited=dict()
        return self.recur(1 ,  [i for i in range(1 , N+1)] , visited)
    def recur(self , idx , nums , visited):
        if not nums:
            return 1
        status=(idx ,  tuple(nums) )
        if status in visited:
            return visited[status]
        ans=0
        for i , n  in enumerate(nums):
            if idx%n==0 or n%idx==0:
                ans+=self.recur(idx+1 , nums[:i]+nums[i+1:] , visited)
        visited[status]=ans
        return ans


test=Solution()
test.countArrangement(3)