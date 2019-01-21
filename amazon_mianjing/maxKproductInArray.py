# Maximum product of subsequence of size k
# Given an array A[] of n integers, the task is to find a subsequence of size k whose product is maximum among all possible k sized subsequences of given array.
#
# Constraints
#
# 1 <= n <= 10^5
# 1 <= k <= n
# Examples:
#
# Input : A[] = {1, 2, 0, 3},
#           k = 2
# Output : 6
# Explanation : Subsequence containing elements
# {2, 3} gives maximum product : 2*3 = 6
#
# Input : A[] = {1, 2, -1, -3, -6, 4},
#           k = 4
# Output : 144
# Explanation : Subsequence containing {2, -3,
# -6, 4} gives maximum product : 2*(-3)*(-6)*4
# = 144

class Problem:
    def solve(self , nums , k):
        # max(nums)==0
        # max(nums)<0
        # max(nums)>0 and k is odd
        # max(nums>0 ) and k is even
        l=len(nums)
        nums.sort()
        print(nums)
        if nums[-1]==0:
            return 0
        elif nums[-1]<0:
            ans=1
            for i in range(k):
                ans*=nums[l-1-i]
            return ans
        else:
            ans=1
            if k%2==1:
                ans*=nums[-1]
                nums
                k-=1
                l-=1
            s=0
            e=l-1

            while s<l and k>0:
                left=nums[s]*nums[s+1]
                right=nums[e]*nums[e-1]
                if left>right:
                    ans*=left
                    s+=2

                else:
                    ans*=right
                    e-=2
                k-=2
            return ans


test=Problem()
print(test.solve([1, 2, -1, -3, -6, 4] , 4))

