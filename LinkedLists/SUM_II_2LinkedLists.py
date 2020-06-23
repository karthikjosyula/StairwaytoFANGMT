# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = 0, 0
        while l1:
            n1*=10
            n1+=l1.val
            l1 = l1.next if l1.next else None
        while l2:
            n2*=10
            n2+=l2.val
            l2 = l2.next if l2.next else None
        finalsum = n1+n2
        prev = ListNode(-1)
        head = prev
        for i in str(finalsum):
            n = ListNode(i) #creating a listnode with current element i
            head.next = n #linking the prev node's next to current element
            head = n #making the latest listnode as current
        return prev.next  