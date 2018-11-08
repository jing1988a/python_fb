# Given a List of intervals, the length of each interval is 1000, such as [500,1500], [2100,3100].Give a number arbitrarily and determine if the number belongs to any of the intervals.return True or False.
#
# Example
# Given:
#
# List = [[100,1100],[1000,2000],[5500,6500]]
# number = 6000
# Return: True


class Solution:
    """
    @param intervalList:
    @param number:
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        # Write your code here
        # O(n) is simple , can we do O(logN)
        # inclusive or exclusive
        # if is sorted. do below
        # l=len(intervalList)
        # if l==0:
        #     return "False"
        # start=0
        # end=l-1
        # while start<=end:
        #     mid=(start+end)//2
        #     if number-intervalList[mid][0]<=1000:
        #         return "True"
        #     elif number-intervalList[mid][0]>1000:
        #         start=mid+1
        #     else:
        #         end=mid-1
        # return "False"

        l=len(intervalList)
        i=0
        while i <l:
            if number>=intervalList[i][0] and intervalList[i][1]>=number:
                return "True"
            i+=1

        return "False"


# a=[[-203653,-202653],[-288256,-287256],[19396,20396],[835984,836984],[-976643,-975643],[368729,369729],[501747,502747],[847647,848647]]
#
#
# b=368722
#
# test=Solution()
# print(test.isInterval(a , b))




































