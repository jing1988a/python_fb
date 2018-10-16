# import heapq
# class Solution:
#     """
#     @param lists: a list of ListNode
#     @return: The head of one sorted list.
#     """
#     def mergeKLists(self, lists):
#         # write your code here
#         hq=[]
#         for l in lists:
#             if l:
#                 heapq.heappush(hq , [l.val , l ])
#         dummy=ListNode(-1)
#         cur=dummy
#         while hq:
#             nVal , n=heapq.heappop(hq)
#             cur.next=n
#             cur=cur.next
#             if n.next:
#                 heapq.heappush(hq , [n.next.val , n.next])
#         return dummy.next
# class ListNode(object):
#
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
#
# test=Solution()
# a=ListNode(0)
# b=ListNode(1)
# c=ListNode(2)
# a.next=b
# b.next=c
# test.mergeKLists([a])
# [0->1->2->3->null]





class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        s=set(num)
        print(s)
        if not num:
            return 0
        ans=1
        for n in num:
            if n-1 in s:
                continue
            candidate=1
            cur=n
            while cur+1 in s:
                candidate+=1
                cur+=1
            ans=max(ans , candidate)
        return ans


test=Solution()
test.longestConsecutive([3,1,4,1,5,9,2,6,5])

