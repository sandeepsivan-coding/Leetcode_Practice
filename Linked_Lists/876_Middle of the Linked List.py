# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        p1=head
        p2=head
        while p2!=None and p2.next!=None:
            p1=p1.next
            p2=p2.next.next
        return p1