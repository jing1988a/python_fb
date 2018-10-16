# Given a non-repeating prime array arr, and each prime number is used at most once, find all the product without duplicate and sort them from small to large.
#
# Example
# Given arr = [2,3], return [6].
#
# Explanation:
# 2 * 3 = 6.
# Gven arr = [2,3,5], return [6,10,15,30].
#
# Explanation:
# 2 * 3 = 6, 2 * 5 = 10, 3 * 5 = 15, 2 * 3 *5 = 30。


class Solution:
    """
    @param arr: The prime array
    @return: Return the array of all of prime product
    """
    def getPrimeProduct(self, arr):
        # Write your code here
        ans=[]
        l=len(arr)
        if l==0:
            return []
        self.dfs(arr , 0 , l , 1 , ans , 0)
        ans.sort()
        return ans
    def dfs(self , arr , idx , l , candidate , ans , count):
        if count>1:
            ans.append(candidate)
        if idx==l:
            return
        for i in range(idx , l):
            candidate*=arr[i]
            self.dfs(arr , i+1 , l , candidate , ans , count+1)
            candidate//=arr[i]