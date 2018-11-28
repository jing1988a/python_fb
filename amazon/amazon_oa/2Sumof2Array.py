#     pair IDs. 两个数组的数字配对, 然后找出最大的但不超过给定数字M的所有组合. \
#     直接暴力两重循环即可
import sys


class Problem:
    def solve(self, nums1, nums2, maxDis):
        ans = []
        l1 = len(nums1)
        if l1 == 0:
            return []
        l2 = len(nums2)
        if l2 == 0:
            return []
        nums1.sort(key=lambda x: -1 if len(x) != 2 else x[1])
        nums2.sort(key=lambda x: -1 if len(x) != 2 else x[1])
        curSum = -sys.maxsize
        i = 0
        j = l2 - 1
        while i < l1 and j >= 0:
            if len(nums1[i]) != 2:
                i += 1
                continue
            if len(num2[j]) != 2:
                j -= 1
                continue
            temp = nums1[i][1] + nums2[j][1]
            if temp <= maxDis:
                if temp > curSum:
                    ans = [[nums1[i][0], nums2[j][0]]]
                    curSum = temp
                elif temp == curSum:
                    ans.append([nums1[i][0], nums2[j][0]])
                i += 1
            elif temp > maxDis:
                j -= 1
        return ans


test = Problem()
num1 = [[1, 8000], [2, 9000]]
num2 = [[0, 1000],[1, 2000], [2, 3000], [3, 4000], [4, 5000]]

print(test.solve(num1, num2, 10000))


#  its very easy to think of a brute force way which is using 2 for loops to check every combination and keep update
#  result and curentMax. which has a runtime of O(n^2) , to improve a O(n^2) rintime code, it is easy to think about
#  try hashtable to imporve it to O(n) or sort it to see if we can imporve it to O(nlogn).
#  if this question want find pairs that exactly match maxDis, then obviously hastable is the way to go.
#  but it want return the closest to maxDis then sort and then using a 2 pointer algrithom is the way to go
