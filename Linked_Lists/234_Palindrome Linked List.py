# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        fast=head
        slow=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        prev=None
        nxt=None
        curr=slow.next
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        p1=head
        p2=prev
        while p2:
            if p1.val!=p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True