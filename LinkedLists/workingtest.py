# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None):
            return None
        elif (headB == None):
            return None
        else:
            n1 = 0
            n2 = 0
            l1 = headA
            l2 = headB
            while l1 or l2:
                if l1:
                    n1 += 1
                    l1 = l1.next if l1.next else None
                if l2:
                    n2 += 1
                    l2 = l2.next if l2.next else None
            Diff = abs(n1 - n2)
            while headA or headB:
                if n1 > n2:
                    while Diff > 0:
                        headA = headA.next
                        Diff -= 1
                elif n2 > n1:
                    while Diff > 0:
                        headB = headB.next
                        Diff -= 1
                p = headA.val
                q = headB.val
                if p == q:
                    return headB
                else:
                    headA = headA.next if headA.next else headA.next
                    headB = headB.next if headB.next else headB.next
            return None

