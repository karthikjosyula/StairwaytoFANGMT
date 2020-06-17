# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # recursive approach
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

"""
        #Iterative approach
        prev = ListNode(-1)
        head = prev
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next if l1.next else None
            else:
                head.next = l2
                l2 = l2.next if l2.next else None
            head = head.next        
        head.next = l1 if l1 is not None else l2
        return prev.next
"""