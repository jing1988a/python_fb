# 感谢地里的推荐，可惜没过。
# 电面：
# 有一堆log，每行的格式是“时间点：各种操作”；给定两个时间点，求在这两个时间点（start， end）内的log lines。假设log非常大。
# 给了一些函数，比如：goToOffset(), getLine(), getCurrentOffset(), fileSize() 和一些基本的文本操作。
#
# 我的解法是，二分法查找开始的时间点（start），然后从这个时间点往前找到最早出现的同一时间点（start），有点类似Leetcode 81的解法（不过是sorted）。


class Problem:
    def solve(self, nums, a, b):

        i = self.getLeftEdge(nums, a)
        j = self.getRightEdge(nums, b)
        # print(i)
        # print(j)
        return j - i + 1

    def getLeftEdge(self, nums, a):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] >= a:
                j = mid - 1
            else:
                i = mid + 1
        return i

    def getRightEdge(self, nums, a):
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] <= a:
                i = mid + 1
            else:
                j = mid - 1
        return j


nums = [1, 2, 3, 3, 3, 4, 5, 6, 6]
a = 3
b = 6
test = Problem()
print(test.solve(nums, a, b))
