# Python program to perform iterative preorder traversal

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# An iterative process to print preorder traveral of BT
def iterativePreorder(root):
    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while (len(nodeStack) > 0):

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.data),

        # Push right and left children of the popped node
        # to stack
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

        # Driver program to test above function


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
iterativePreorder(root)

#Spae optimized O(1) space : Time : O(N)
# Tree Node
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


# Iterative function to do Preorder traversal of the tree
def preorderIterative(root):
    if (root == None):
        return

    st = []

    # start from root node (set current node to root node)
    curr = root

    # run till stack is not empty or current is
    # not NULL
    while (len(st) or curr != None):

        # Print left children while exist
        # and keep appending right into the
        # stack.
        while (curr != None):

            print(curr.data, end=" ")

            if (curr.right != None):
                st.append(curr.right)

            curr = curr.left

        # We reach when curr is NULL, so We
        # take out a right child from stack
        if (len(st) > 0):
            curr = st[-1]
            st.pop()

        # Driver Code


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.left.left = Node(70)
root.left.right = Node(50)
root.right.left = Node(60)
root.left.left.right = Node(80)

preorderIterative(root)

# This code is contributed by Arnab Kundu



