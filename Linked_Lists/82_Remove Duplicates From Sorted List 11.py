# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        curr=head
        if curr==None or curr.next==None:
            return head
        while curr!=None:
            if curr.next!=None and curr.val==curr.next.val:
                dup=curr.val
                while curr!=None and  curr.val==dup:
                    curr=curr.next
                prev.next=curr
            else:
                prev=curr
                curr=curr.next
        return dummy.next