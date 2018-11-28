# Given an array, find two numbers in the array and their sum is closest to the target value but does not exceed the target value, return their sum.
#
# Example
# Input:target = 15
# array = [1,3,5,11,7]
# Output:14
# Notice
# if there is no result meet the requirement, return -1.

import sys
class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        # Write your code here
        l=len(array)
        if l<2:
            return -1
        array.sort()
        i=0
        j=l-1
        curMax=-sys.maxsize
        while i <j:
            temp=array[i]+array[j]
            if temp==target:
                return target
            elif temp<target:
                if temp>curMax:
                    curMax=temp
                i+=1
            else:
                j-=1
        return curMax if curMax != -sys.maxsize else -1
