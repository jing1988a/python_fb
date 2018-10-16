# Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.
#
# Person A will NOT friend request person B (B != A) if any of the following conditions are true:
#
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.
# Note that if A requests B, B does not necessarily request A. Also, people will not friend request themselves.
#
# How many total friend requests are made?
#
# Example
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
#
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
#
# Input: [20,30,100,110,120]
# Output: 3
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
#
# Notice


class Solution:
    """
    @param ages:
    @return: nothing
    """
    def numFriendRequests(self, ages):
        #
        d=collections.defaultdict(int)
        for a in ages:
            d[a]+=1
        ans=0
        for i in d.keys():
            for j in d.keys():
                if self.willRequest(i , j):
                    if i==j:
                        ans+=d[i]*(d[i]-1)
                    else:
                        ans+=d[i]*d[j]
        return ans

    def willRequest(self , a , b ):
        return not (b<=(0.5*a+7) or b>a or (b>100 and a<100))