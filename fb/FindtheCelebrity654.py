"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        candidates=[True for i in range(n) ]
        for i in range(n):
            if candidates[i]==True:
                j=0
                while j<n:
                    if i==j:
                        j+=1
                        continue
                    if Celebrity.knows(i , j) or not Celebrity.knows(j , i):
                        candidates[i]=False
                        break
                    else:
                        candidates[j]=False
                    j+=1
                if j==n:
                    return i
        return -1

class Celebrity:
    def knows(self , i , j):
        return True