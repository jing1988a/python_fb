import collections
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        # write your code here
        numbers.sort()
        l = len(numbers)
        if l < 4:
            return []
        ans = set()
        d = collections.defaultdict(list)
        for i in range(l - 3):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, l - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                d[target - numbers[i] - numbers[j]].append([i, j])
        for i in range(2, l - 1):

            for j in range(i + 1, l):

                if numbers[i] + numbers[j] in d:
                    for a, b in d[numbers[i] + numbers[j]]:
                        if b < i:
                            ans.add((numbers[a], numbers[b], numbers[i], numbers[j]))
        return list(ans)


test=Solution()
print(test.fourSum([1,0,-1,-1,-1,-1,0,1,1,1,2] , 2 ))

# Output
# [[-1,0,1,2],[0,0,1,1]]
# Expected
# [[-1,0,1,2],[-1,1,1,1],[0,0,1,1]]