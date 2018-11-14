# We are given an array of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
#
# Example
# Input:
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation:
# The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
#
# Input:
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation:
# The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
#
# Notice
# The length of asteroids will be at most 10000.
# Each asteroid will be a non-zero integer in the range [-1000, 1000]..


class Solution:
    """
    @param asteroids: a list of integers
    @return: return a list of integers
    """

    def asteroidCollision(self, asteroids):
        # write your code here
        l = len(asteroids)
        if l == 0:
            return []
        ans=[]
        i=0
        while i<l:
            if asteroids[i]<0:
                if not ans or ans[-1]<0:
                    ans.append(asteroids[i])
                elif ans[-1]<-asteroids[i]:
                    i-=1
                    ans.pop()
                elif ans[-1]==-asteroids[i]:
                    ans.pop()
            else:
                ans.append(asteroids[i])
            i+=1
        return ans


        # l = len(asteroids)
        # if l == 0:
        #     return []
        # rightStack = []
        # leftStack = []
        # for a in asteroids:
        #     if a < 0:
        #         destroyed=False
        #         while rightStack:
        #             cur = rightStack[-1]
        #             if cur == -a:
        #                 rightStack.pop()
        #                 destroyed=True
        #                 break
        #             elif cur > -a:
        #                 destroyed = True
        #                 break
        #             else:
        #                 rightStack.pop()
        #         if not destroyed:
        #             leftStack.append(a)
        #     else:
        #         rightStack.append(a)
        #     # print(rightStack)
        #     # print(leftStack)
        #     # print("")
        # return  leftStack+rightStack

test=Solution()
print(test.asteroidCollision([7,-1,2,-3,-6,-6,-6,4,10,2]))

