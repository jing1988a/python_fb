# There are n group children ready to go on a spring tour. The array a indicates the number of people in each group. There are no more than four people in each group. There are now several cars. Each car can only take up to four people. The same group of children must sit in the same car, and each car need't be full. Ask how many cars you need to meet the travel needs of your children.
#
# Example
# Given a = [1,2,3,4]，return 3.
#
# At this time, there are 4 people in the fourth group, sitting alone in a car.
# The first group has 1 person, the third group has 3 people, and just 4 people get for one car.
# The second group of 2 people has a single car, so at least 3 cars are needed.
# Given a = [1,2,2,2]，return 2.
#
# Explanation:
# The first group and the second group get one car
# The third group and the fourth group get one car
# Therefore, at least two cars are needed.
# Notice
# 0 \leq n \leq 1e40≤n≤1e4
# 1 \leq a[i] \leq 41≤a[i]≤4


class Solution:
    """
    @param a: The array a
    @return: Return the minimum number of car
    """
    def getAnswer(self, a):
        # Write your code here
        counter=collections.Counter(a)
        # print(counter)
        ans=0
        ans+=counter[4]
        ans+=counter[3]
        counter[1]=max(0 , counter[1]-counter[3])
        ans+=counter[2]//2
        if counter[2]%2:
            ans+=1
            counter[1]=max(0 , counter[1]-2)
        ans+=counter[1]//4
        if counter[1]%4:
            ans+=1
        return ans