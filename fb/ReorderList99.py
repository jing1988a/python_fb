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
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        dummy=ListNode(-1)
        dummy.next=head
        start=end=dummy
        while end and end.next:
            end=end.next.next
            start=start.next
        rHead=start.next
        start.next=None
        lHead=dummy.next
        rHead=self.reverse(rHead)
        while rHead:
            t1=lHead.next
            t2=rHead.next
            lHead.next=rHead
            rHead.next=t1
            lHead=t1
            rHead=t2
        return dummy.next
    def reverse(self , root):
        pre=None
        cur=root
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre