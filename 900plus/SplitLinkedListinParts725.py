# Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
#
# The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.
#
# The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
#
# Return a List of ListNode's representing the linked list parts that are formed.
#
# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
# Example 1:
# Input:
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a ListNode is [].
# Example 2:
# Input:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
# Note:
#
# The length of root will be in the range [0, 1000].
# Each value of a node in the input will be an integer in the range [0, 999].
# k will be an integer in the range [1, 50].


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if k==0:
            raise Exception('invalid K')
        dummy=ListNode(-1)
        dummy.next=root
        cur=dummy
        total=0
        while cur.next:
            cur=cur.next
            total+=1

        size=total//k
        extra=total%k
        cur=dummy
        ans=[]
        for i in range(k):

            ans.append(cur.next)
            temp=ListNode(-1)
            temp.next=(cur.next)
            cur.next=None
            cur=temp
            for _ in range(size):
                cur=cur.next
            if extra:
                cur=cur.next
                extra-=1
        return ans


# Input:
# [1,2,3,4]
# 5
# Output:
# [[1,2,3,4],[2,3,4],[3,4],[4],[]]
# Expected:
# [[1],[2],[3],[4],[]]
