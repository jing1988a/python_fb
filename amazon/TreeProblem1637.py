# Given a tree of n nodes. The ith node's father is fa[i-1] and the value of the ith node is val[i-1]. Especially, 1 represents the root, 2 represents the second node and so on. We gurantee that -1 is the father of root(the first node) which means that fa[0] = -1.
# The average value of a subtree is the result of the sum of all nodes in the subtree divide by the number of nodes in it.
# Find the maximum average value of the subtrees in the given tree, return the number which represents the root of the subtree.
#
# Example
# Given fa=[-1,1,1,2,2,2,3,3], representing the father node of each point, and val=[100,120,80,40,50,60,50,70] , representing the value of each node, return 1.
#
# Sample diagram：
#                       -1  ------No.1
#                     /     \
#          No.2 ----1        1---------No.3
#                /  |  \     /  \
#               2   2   2    3   3
# No.1 node is (100+120+80+40+50+60+50+70) / 8 = 71.25
# No.2 node are (120 + 40 + 50 + 60) / 4 = 67.5
# No.3 node are (80+50+70) / 3 = 66.6667
# So return 1.
# Notice
# the number of nodes do not exceed 100000
# If there are more than one subtree meeting the requirement, return the minimum number.
#





class Solution:
    """
    @param fa: the father
    @param val: the val
    @return: the biggest node
    """

    # brute force find 1 , then 2 , then 3
    # can we do recursive?
    # is the fa list sorted?


    def treeProblem(self, fa, val):
        # Write your code here
        l = len(fa)
        lv=len(val)
        if l == 0 or lv != l:
            return -1
        # do it backward
        temp = [[0, 0] for i in range(l + 1)]
        for i in range(l , 0, -1):
            # print(i)
            temp[i][0] += val[i - 1]
            temp[i][1] += 1
            if i!=1:
                temp[fa[i-1]][0] += temp[i][0]
                temp[fa[i-1]][1] += temp[i][1]
        maxV=0
        ans=-1
        for i in range(1 , l+1):
            if temp[i][0]/temp[i][1]>maxV:
                maxV=temp[i][0]/temp[i][1]
                ans=i
        return ans
# Given fa=[-1,1,1,2,2,2,3,3], representing the father node of each point, and val=[100,120,80,40,50,60,50,70] , representing the value of each node, return 1.
#
# Sample diagram：
#                       -1  ------No.1
#                     /     \
#          No.2 ----1        1---------No.3
#                /  |  \     /  \
#               2   2   2    3   3
# No.1 node is (100+120+80+40+50+60+50+70) / 8 = 71.25
# No.2 node are (120 + 40 + 50 + 60) / 4 = 67.5
# No.3 node are (80+50+70) / 3 = 66.6667
# So return 1.
fa=[-1,1,1,2,2,2,3,3]
val=[100,120,80,40,50,60,50,70]
test=Solution()
print(test.treeProblem(fa , val))






























