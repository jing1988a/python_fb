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
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        pre=ListNode(-1)
        pre.next=head
        start=end=pre
        for i in range(m-1):
            start=start.next
        for i in range(n):
            end=end.next
        cur=start.next
        while start.next!=end:
            temp=cur.next
            cur.next=temp.next
            temp.next=start.next
            start.next=temp
        return pre.next