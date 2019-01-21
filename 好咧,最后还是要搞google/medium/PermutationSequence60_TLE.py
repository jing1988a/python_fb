# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note:
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:
#
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
#
# Input: n = 4, k = 9
# Output: "2314"

import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str



        Given n will be between 1 and 9 inclusive.
        think about return all list.



        """
        if k>math.factorial(n):
            return None
        self.k=k
        nums=[i for  i in range(1 , n+1)]
        #ans=None# 这个不行 NONE 和 STR 都不是传的REFERRENCE 在函数里改变值不会改变外面的值
        global ans
        ans=None
        self.find_ans_flag=False
        def dfs( candidate , nums ):
            global ans
            if self.find_ans_flag:
                return
            # print(nums)
            # print(candidate)
            if not nums:
                self.k-=1
                if self.k==0:
                    ans=''.join(list(map(str , candidate)))# python3 的MAP 返回时迭代器
                    self.find_ans_flag=True
                    return
            for i in range(len(nums)):
                candidate.append(nums[i] )
                dfs( candidate , nums[:i]+nums[i+1:])
                candidate.pop()

        #dfs( [] , nums)

        #上面是可行的  但是dfs( candidate , nums[:i]+nums[i+1:])  这一步太慢了
        def dfs2( candidate , n ,l):
            global ans
            if self.find_ans_flag:
                return
            # print(nums)
            # print(candidate)
            # print(' ')
            if l== n:
                self.k-=1
                if self.k==0:
                    ans=''.join(list(map(str , candidate)))# python3 的MAP 返回时迭代器
                    self.find_ans_flag=True
                    return
            for i in range(1 , n+1):
                if i not in candidate:
                    candidate.append(i)
                    dfs2( candidate  , n , l+1 )
                    candidate.pop()
        dfs2([] , n , 0)
        return ans
    #肯定有数学算法的






#         self.count=0
#         self.ans=""
#         self.k=k
#         self.l=n
#         self.available=[x for x in range(1 , n+1)]
# #         def recurPermu(  cur , available):
# #             if self.ans: #
# #                 return   #




# #             if not available:
# #                 #when available is empty we found a result
# #                 self.count+=1                    #
# #                 if self.count==self.k:           #
# #                     self.ans=cur                 #



# #                 return


# #             for i in range(len(available)):
# #                 recurPermu(cur+str(available[i]) , available[:i]+available[i+1:])


# #             return





# #         recurPermu(  "" , available)

# #         return self.ans

#         #下面爸爸教你用DFS 做这道理。  好吧 其实上面的也是DFS



#         def dfs(cur_str):
#             # print(cur_str)
#             # print(self.k)
#             if self.ans:
#                 return

#             if len(cur_str)==self.l:
#                 self.k-=1

#                 if self.k==0:
#                     self.ans=cur_str


#             for i in range(0 , self.l):


#                 if self.available[i] not in cur_str:
#                     dfs(cur_str+[self.available[i]])

# #         def dfs2(cur_str):

# #             if self.ans:
# #                 return

# #             if len(cur_str)==self.l:
# #                 self.k-=1

# #                 if self.k==0:

# #                     self.ans=cur_str[:]


# #             for i in range(1 , self.l+1):
# #                 if i not in cur_str:


# #                     cur_str.append(i)
# #                     dfs2(cur_str)
# #                     cur_str.pop()
#         dfs([])
#         print(self.ans)
#         return ''.join(list(map(str , self.ans)) )



