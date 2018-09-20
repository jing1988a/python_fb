"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head:
            return head
        cur=head
        i=1
        while cur.next:
            cur=cur.next
            i+=1
        end=cur
        k=k%i
        pre=ListNode(-1)
        pre.next=head
        fast=pre
        i=0;
        while i<k:
            fast=fast.next
            i+=1
        slow=pre
        while fast.next:
            slow=slow.next
            fast=fast.next
        if slow==pre:
            return pre.next
        else:
            end.next=pre.next
            res=slow.next
            slow.next=None
            return res

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next