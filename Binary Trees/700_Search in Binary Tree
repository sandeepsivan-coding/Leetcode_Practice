# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, target):
        if root==None:
            return None
        curr=root 
        while curr!=None:
            if curr.val==target:
                return curr
            elif curr.val>target:
                curr=curr.left
            else:
                curr=curr.right
        return None