# Given a 2D array, and each line has only 0 and 1, the front part is 0, and the latter part is 1. Find the number of columns in the leftmost 1 of all the rows in the array.
#
# Example
# Given arr = [[0,0,0,1],[1,1,1,1]], return 0.
#
# Explanation:
# Arr[1][0] is the leftmost 1 in all rows and its column is 0.
# Given arr = [[0,0,0,1],[0,1,1,1]], return 1.
#
# Explanation:
# Arr[1][1] is the leftmost 1 in all rows and its column is 1.
# Notice
# The number of rows in the array and the number of columns do not exceed 1000
# In order to limit the time complexity, your program will run 50000 times


class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        # Write your code here
        n=len(arr)
        if n==0:
            return 0
        m=len(arr[0])
        if m==0:
            return 0

        s=0
        e=m-1
        while s<=e:
            mid=(s+e)//2
            if self.hasOne(arr , mid , n):
                e=mid-1
            else:
                s=mid+1
        # print(e)
        # print(s)
        if e==-1:
            return 0
        return e if self.hasOne(arr , e , n) else s
    def hasOne(self , arr , mid , n):
        for i in range(n):
            if arr[i][mid]==1:
                return True
        return False