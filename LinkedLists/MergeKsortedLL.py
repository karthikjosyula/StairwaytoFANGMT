# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []  # declar an array called nodes
        head = point = ListNode(0)  # Initialize a linkedlist name it head and point
        for l in lists:  # loop through all the lists
            while l:
                self.nodes.append(l.val)  # append values to the array
                l = l.next  # increment the nodes
        for x in sorted(self.nodes):  # sort all the values in array
            point.next = ListNode(x)  # for current element in array point the next node in LL
            point = point.next
        return head.next