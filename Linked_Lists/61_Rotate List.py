# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        l=1
        curr=head
        while curr.next!=None:
            curr=curr.next
            l+=1
        k=k%l
        if k==0:
            return head

        p1=head
        p2=head
        for i in range(k):
            p1=p1.next
        while p1.next!=None:
            p1=p1.next
            p2=p2.next
        p1.next=head
        head=p2.next
        p2.next=None
        return head