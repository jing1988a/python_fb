class Problem:
    def solve(self , nums):
        for i in range(len(nums)):
            while nums[i]!=i:
                if nums[nums[i]]==nums[i]:
                    return nums[i]
                nums[nums[i]] , nums[i]=nums[i] , nums[nums[i]]
                print(nums)
        return None


test=Problem()
print(test.solve([ 1 , 2 , 2  , 2 , 3 , 4 ]))
