import  sys
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: three non-overlapping subarrays with maximum sum
    """
    def maxSumOfThreeSubarrays(self, nums, k):
        # Write your code here
        l=len(nums)
        if l<3*k:
            return []
        dp=[]
        i=0
        cur=0
        while i <l:
            cur+=nums[i]
            if i>=k:
                cur-=nums[i-k]
            if i>=k-1:
                dp.append(cur)
            i+=1
        l=len(dp)
        leftMax=dp[0]
        leftIdx=0
        lList=[0 for _ in range(l)]
        lList[0]=0
        for i in range(1 , l):
            if leftMax < dp[i]:
                leftIdx = i
                leftMax = dp[i]
            lList[i]=leftIdx


        rightMax=dp[l-1]
        rightIdx=l-1
        rList=[0 for _ in range(l)]
        rList[l-1]=rightIdx
        for i in range(l-2 , -1 , -1):
            if rightMax < dp[i]:
                rightIdx = i
                rightMax = dp[i]
            rList[i]=rightIdx

        curMax=-sys.maxsize
        x=y=z=None
        for i in range(k , l-k):
            if dp[i]+dp[lList[i-k]]+dp[rList[i+k]]>curMax:
                curMax=dp[i]+dp[lList[i-k]]+dp[rList[i+k]]
                x=lList[i-k]
                y=i
                z=rList[i+k]
        return [x , y , z]

test=Solution()
print(test.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1] , 2))
# Output
# [0,4,6] 12 26 75
# Expected
# [0,3,5]