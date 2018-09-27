"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        lDummy=ListNode(-1)
        rDummy=ListNode(-1)
        cur=head
        lCur=lDummy
        rCur=rDummy
        while cur:
            if cur.val<x:
                lCur.next=cur
                cur=cur.next
                lCur=lCur.next
                lCur.next=None
            else:
                rCur.next=cur
                cur=cur.next
                rCur=rCur.next
                rCur.next=None
        lCur.next=rDummy.next
        return lDummy.next