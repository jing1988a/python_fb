"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        pre=None
        cur=head
        while cur:
            if pre is None or cur.val!=pre.val:
                pre=cur
                cur=cur.next
            else:
                pre.next=cur.next
                cur=cur.next
        return head