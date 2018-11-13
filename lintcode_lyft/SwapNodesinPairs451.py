# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Challenge
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
#

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
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        if not head:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        while pre.next and pre.next.next:
            temp=pre.next
            pre.next=pre.next.next
            temp.next=temp.next.next
            pre.next.next=temp
            pre=pre.next.next
        return dummy.next
