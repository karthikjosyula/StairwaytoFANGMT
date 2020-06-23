# Definition for singly-linked list.
class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        def reverseList(self, head):
            prev= None
            curr = head
            while curr:
                curr.next, prev, curr  = prev, curr, curr.next
            return prev
