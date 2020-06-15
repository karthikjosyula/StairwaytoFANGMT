from collections import deque
llist = deque("abcdefg")
print(llist)
print("---------")
print("Inserting a new element to the right")
llist.append('k')
print(llist)
print("---------")
print("Deleting the newly inserted element from right")
llist.pop()
print(llist)
print("---------")
print("inserting new element to left")
print(llist)
llist.appendleft('i')
llist.appendleft('j')
print(llist)
print("---------")
print("Deleting the newly inserted element from left")
llist.popleft()
print(llist)
"""
Creating our own linkedlist
"""
print("===============================")
print("Creating own linkedlist")

class Node:
    def __int__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class LinkedList:
    def __int__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "-> ".join(nodes)

llist = LinkedList()
llist

first_node = Node("a")
llist_head = first_node
llist

second_node = Node("b")
first_node.next = second_node
third_node = Node("c")
second_node.next = third_node
llist




"""
Traversing through a linked list
"""
print("==================================")
print("Traversing through a linked list")
def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = next.node
llist = deque(['q','b','c','d','h'])
llist
for node in llist:
    print(node)
    print(llist.head())


