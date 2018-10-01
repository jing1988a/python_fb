class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        ans=[]
        nums.sort()
        l=len(nums)
        self.recur(nums ,  0 , l , [] , ans)
        return ans
    def recur(self , nums , start , l , candidate , ans):
        ans.append(candidate[:])
        for i in range(start , l):
            if i!=start and nums[i]==nums[i-1]:
                continue
            candidate.append(nums[i])
            self.recur(nums , i+1 , l , candidate , ans)
            candidate.pop()