"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        pre=None
        while head is not None:
            temp=head.next
            head.next=pre
            pre=head
            head=temp
        return pre
