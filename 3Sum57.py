import collections
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        l=len(numbers)
        if l<3:
            return []
        ans=set()
        numbers.sort()
        d=collections.defaultdict(list)
        for i in range(l-1):
            for j in range(i+1 , l):
                d[-(numbers[i]+numbers[j])].append([i , j])
        for k in range(2 , l):
            if numbers[k] in d:
                for candidate in d[numbers[k]]:
                    if k>candidate[1]:
                        ans.add(  (numbers[candidate[0]] , numbers[candidate[1]] , numbers[k]) )
        return list(ans)

