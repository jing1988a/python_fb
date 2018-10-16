# Given an array Ages of length n, where the first i elements represent the age of the individual i. Find total number of friend requests sent by this n person. There are some requirements:
#
# if Age(B) <= (1/2)Age(A) + 7, A will not send a request to B.
# if Age(B) > Age(A), A will not send a request to B.
# if Age(B) < 100 and Age(A) > 100, A will not send a request to B.
# If it does not satisfy 1,2,3, then A will send a request to B
# Example
# Given Ages = [10,39,50], return 1.
#
# Explanation:
# Only people of age 50 will send friend requests to people of age 39.
# Given Ages = [101,79,102], return 1.
#
# Explanation:
# Only people of age 102 will send friend requests to people of age 101.
# Notice
# Ages.length <= 1000。
# Everyone's age is greater than 0, less than 150。



class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def friendRequest(self, ages):
        # Write your code here
        l=len(ages)
        if l<2:
            return 0
        ans=0
        for i in range(l):
            for j in range(l):
                if i==j:
                    continue
                if self.willRequest(ages[i] , ages[j]):
                    ans+=1
        return ans
    def willRequest(self , a , b):
        return not( b<=(a/2+7) or b>a or (b<100 and a>100))