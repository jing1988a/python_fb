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
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        dummy=ListNode(-1)
        pre=dummy
        dummy.next=head
        cur=head
        while cur:
            if cur.val==val:
                pre.next=cur.next
                cur=cur.next
            else:
                pre=cur
                cur=cur.next
        return dummy.next